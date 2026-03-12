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
