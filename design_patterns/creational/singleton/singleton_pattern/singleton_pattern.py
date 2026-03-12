import threading


class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        print("Initializing Connection...")
        self.connected = True

    def __str__(self):
        return "db is connected"

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1)
print(db2)
print(id(db1), id(db2))

