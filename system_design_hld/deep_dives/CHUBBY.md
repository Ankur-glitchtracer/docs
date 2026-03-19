# Deep Dive: Chubby (Distributed Locking Service)

Google's Chubby is a highly available and persistent distributed lock service and file system. It acts as the "heart of coordination" for massive distributed systems like Google File System (GFS) and BigTable, enabling them to elect masters, manage metadata, and synchronize activities across thousands of nodes.

## 1. Core Architecture & Paxos

A Chubby cell typically consists of five replicas to ensure high availability and fault tolerance.

- **Master Election:** The replicas use the Paxos consensus algorithm to elect a single Master. The Master is granted a lease that all other replicas must honor.  
- **Centralized Control:** To maintain strict consistency (CP in the CAP theorem), only the Master can serve read and write requests. If a client contacts a replica, it is immediately redirected to the current Master.  
- **Majority Rule:** As long as a majority of replicas (e.g., 3 out of 5) are alive and communicating, the Chubby cell remains operational and can reach consensus on state changes.  

## 2. Distributed Locking & Leases

The primary purpose of Chubby is to provide coarse-grained locks—locks that are intended to be held for hours or days, rather than milliseconds.

### Lock Types

- **Exclusive (Write) Lock:** Only one client can hold the lock at a time (e.g., to act as a Master).  
- **Shared (Read) Lock:** Multiple clients can hold the lock simultaneously for reading metadata.  

### Session Lifecycle & KeepAlives

Chubby manages the relationship between the cell and its clients via Sessions, utilizing a complex dance of local and remote timers.

- **Leases & KeepAlives:** Locks are granted using time-bound leases. Clients periodically send KeepAlive RPCs to the Master to renew their session leases.  
- **Local vs. Master Timers:** The client maintains a local lease timeout (a conservative approximation of the Master's actual timer). If the Master fails, the server-side timer halts, but the client's local timer continues counting down.  
- **Jeopardy & Cache Disablement:** If the master election is delayed and the client's local timer expires, the session enters a Jeopardy state. Because the client is unsure if the server terminated its session, it immediately empties and disables its local cache to prevent reading stale data.  
- **Grace Period (45 Seconds):** Entering Jeopardy triggers a 45-second Grace Period. The client actively searches for the newly elected Master.  
- **Recovery:** If it connects within 45 seconds, the lease is extended, and the cache is safely re-enabled.  
- **Expiration:** If the Grace Period ends without contact, the session is forcefully terminated to prevent permanent lock starvation.  

## 3. Client-Side Caching & Invalidation

To handle massive read-heavy workloads without overwhelming the Master, Chubby implements a sophisticated consistent, write-through cache on the client side. Clients cache file contents, node metadata, and open handles in memory.

To maintain absolute consistency, Chubby enforces a strict invalidation protocol:

- **Piggybacked Invalidations:** When the Master receives a write request, it blocks the modification and must invalidate cached copies on all clients holding that data. To save network bandwidth, the Master "piggybacks" this invalidation request onto its reply to the client's next pending KeepAlive call.  
- **Client Acknowledgment:** The client flushes its cache and sends an acknowledgment back to the Master attached to its subsequent KeepAlive call. The Master strictly waits for acknowledgments from all caching clients before applying the write.  
- **Non-Blocking Reads ('Uncachable' State):** Synchronously waiting for every client to acknowledge introduces a dangerous latency window. To prevent read-heavy workloads from blocking during this wait, the Master temporarily marks the file as 'Uncachable'. Any client attempting to read the file during the invalidation window is served the data instantly, but is explicitly instructed by the Master not to cache the result.  

## 4. Integration with GFS & BigTable

Chubby is the foundational component that makes Google’s storage infrastructure possible.

- **BigTable Master Election:** Chubby ensures that only one BigTable Master is active at any time. If the Master loses its Chubby lock, it immediately terminates itself.  
- **Tablet Discovery:** Clients find the "Root Tablet" of a BigTable cluster by reading its location from a specific Chubby file.  
- **Access Control:** BigTable stores its Access Control Lists (ACLs) as small files within the Chubby filesystem for high availability and consistency.  
- **GFS Metadata:** GFS uses Chubby to store the identity of its current Master and to coordinate chunk replication.  

## 5. Visualizing the Interaction

The following diagram illustrates how a client interacts with the Chubby cell for master discovery and configuration.

```mermaid
graph TD
    subgraph "Chubby Cell (5 Replicas)"
        R1((Replica)) --- Master((Master Node))
        R2((Replica)) --- Master
        R3((Replica)) --- Master
        R4((Replica)) --- Master
        Note bottom of Master: Elected via Paxos
    end

    Client[Application Client] -->|1. Find Master| Master
    Client -->|2. Acquire Lock / Read Meta| Master
    Master -->|3. KeepAlive / Invalidate| Client

    subgraph "Dependent System (e.g., BigTable)"
        BT_Master[BigTable Master] -->|Acquire Lock| Master
        BT_Tablet[Tablet Server] -->|Register Presence| Master
    end
```
## 6. Practical Implementation

Explore low-level implementations of distributed consensus and locking:

* [System Design: HDFS High Availability](./HDFS_HIGH_AVAILABILITY.md)
* [System Design: NoSQL Internals](./NOSQL_INTERNALS.md)
* [Infrastructure: Redis Rate Limiter](../../infrastructure_challenges/redis_rate_limiter/PROBLEM.md)
