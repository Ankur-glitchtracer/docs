# Key System Characteristics

Before designing a large-scale distributed system, architects must define the baseline characteristics and Non-Functional Requirements (NFRs) the system must achieve.

## 1. Scalability

Scalability is the capability of a system to handle a growing amount of work or its potential to be enlarged to accommodate that growth.

- **Horizontal Scaling (Scaling Out):** Adding more servers to a pool of resources.  
  - Preferred for distributed systems because it offers near-infinite scalability.  
  - Utilizes cheaper commodity hardware.  
  - Requires stateless application design and complex data partitioning.  

- **Vertical Scaling (Scaling Up):** Upgrading the power of an existing server (more CPU, RAM, faster Disks).  
  - Simpler to implement but has a hard physical ceiling.  
  - Creates a Single Point of Failure (SPOF).  

## 2. Reliability

Reliability is the probability a system will fail in a given period. A distributed system is considered reliable if it keeps delivering its services even when one or several of its software or hardware components fail.

- **Implementation:** Achieved through strict redundancy.  
  - If a server fails, a replica must instantly take its place.  
  - Data must be replicated across multiple physical disks, racks, or geographical data centers.  

## 3. Availability

Availability is the percentage of time a system remains operational and accessible to clients under normal conditions.

- **Measurement:** Measured in "Nines" (e.g., 99.9% uptime = ~8.7 hours downtime/year; 99.999% "Five Nines" = ~5 minutes downtime/year).  
- **Reliability vs. Availability:** A reliable system is inherently available. An available system is not necessarily reliable (e.g., may stay online but return stale/incorrect data due to partial backend failure).  

## 4. Efficiency

Efficiency measures how well a system performs its required tasks, using two primary metrics:

- **Latency (Response Time):** Time required to process a single request and return a response. Modern web systems aim for low latency (< 200ms).  
- **Throughput (Bandwidth):** Number of operations a system can handle over a specific period (e.g., Requests Per Second or MB/s).  

> Note: A system can have high throughput but terrible latency if requests take a long time to process but the system can process millions of them simultaneously.  

## 5. Serviceability / Manageability

Serviceability is the simplicity and speed with which a system can be repaired, maintained, or updated.  

- **Implementation:** Achieved through aggressive automation, CI/CD pipelines, distributed tracing, and centralized logging.  
- If it takes weeks to deploy a database schema change or isolate a bug, the system lacks serviceability.
