# The Object Pool pattern is all about performance optimization. It’s most useful when creating an object is "expensive" (in terms of time or resources) and you need to use those objects frequently but briefly.

# Here is a problem statement designed to help you "feel" the need for this pattern.

# Problem Statement: The High-Performance Database Proxy
# You are building a high-frequency trading application that needs to execute thousands of small database queries per second.

# The Challenge
# Opening a new database connection is a heavy operation. It involves:

# Allocating memory for the connection object.

# Establishing a TCP handshake with the server.

# Authenticating the user.

# If your application creates a new connection for every single query and closes it immediately after, the system will lag due to the overhead of "handshaking," and you might eventually run out of available ports on your machine.

# Your Task
# Create a Connection Pool that manages a limited set of "Database Connection" objects.

# Requirements:

# The Connection Class: Create a class DBConnection that has a unique ID. In its constructor, simulate a delay (e.g., Thread.sleep(500)) to represent the cost of creation.

# The Pool Manager: Implement a ConnectionPool class that:

# Has a Fixed Size (e.g., maximum 5 connections).

# Acquire: Provides a connection to a requester. If one is available in the pool, it returns it immediately. If not, it either waits or creates a new one (up to the max limit).

# Release: When a worker is done, they "return" the connection to the pool instead of destroying it.

# The Test: Write a multi-threaded simulation where 10 workers try to perform tasks simultaneously using only the 5 connections in your pool.

# Things to watch out for (The "Gotchas")
# As you implement this, keep these questions in mind:

# Thread Safety: What happens if two threads try to "Acquire" the last available connection at the exact same millisecond?

# State Reset: When a connection is returned to the pool, how do you ensure the next user doesn't see "leftover" data from the previous user?

# The "Empty" Pool: What should your code do if a thread asks for a connection but the pool is maxed out and all are currently in use? (Wait? Fail? Throw an error?)


from time import sleep
from uuid import UUID, uuid4
from threading import Lock, Semaphore, Thread


class DBConnection:
    def __init__(self) -> None:
        self.id: UUID = uuid4()
        sleep(2)


class ConnectionPool:
    def __init__(self) -> None:
        self.connections: dict[DBConnection, bool] = {}
        self.pool: int = 5
        self.lock = Lock()
        self.semaphore = Semaphore(self.pool)

    def get_db(self) -> DBConnection:
        self.semaphore.acquire()
        with self.lock:
            for conn, is_busy in self.connections.items():
                if not is_busy:
                    self.connections[conn] = True
                    return conn

        new_conn = DBConnection()
        with self.lock:
            self.connections[new_conn] = True

        return new_conn

    def release_connection(self, conn: DBConnection) -> None:
        with self.lock:
            self.connections[conn] = False
        self.semaphore.release()


def worker(pool: ConnectionPool, name: str):
    print(f"Worker {name} is requesting a connection...")
    conn = pool.get_db()
    print(f"Worker {name} secured connection: {conn.id}")
    
    # Simulate doing some "work" with the connection
    sleep(4) 
    
    print(f"Worker {name} is releasing connection: {conn.id}")
    pool.release_connection(conn)

if __name__ == "__main__":
    # Update DBConnection sleep to 1 or 0.5 for testing!
    my_pool = ConnectionPool()
    threads = []

    # Create 10 workers for a pool of size 5
    for i in range(10):
        t = Thread(target=worker, args=(my_pool, f"#{i}"))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        
    print("All workers finished.")
