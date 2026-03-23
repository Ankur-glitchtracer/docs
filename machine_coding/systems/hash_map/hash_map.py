from typing import Generic, TypeVar, List, Optional

K = TypeVar('K')
V = TypeVar('V')


class HashItem(Generic[K, V]):
    """Represents a key-value pair stored in the hash table.
    
    Attributes:
        key (K): The unique identifier for the item.
        value (V): The data associated with the key.
    """

    def __init__(self, key: K, value: V) -> None:
        """Initializes a new HashItem.

        Args:
            key (K): The key to identify the item.
            value (V): The value to store.
        """
        self.key: K = key
        self.value: V = value


class HashTable(Generic[K, V]):
    """A Hash Table implementation using separate chaining for collision resolution.
    
    Attributes:
        size (int): The total number of buckets in the hash table.
        table (List[List[HashItem[K, V]]]): The underlying array of buckets.
    """

    def __init__(self, size: int) -> None:
        """Initializes the HashTable with a fixed number of buckets.

        Args:
            size (int): The number of buckets.
        """
        self.size: int = size
        self.table: List[List[HashItem[K, V]]] = [[] for _ in range(self.size)]

    def _hash_function(self, key: K) -> int:
        """Calculates the bucket index for a given key.

        Args:
            key (K): The key to hash.

        Returns:
            int: The computed bucket index (0 to size - 1).
        """
        return hash(key) % self.size

    def set(self, key: K, value: V) -> None:
        """Inserts or updates a key-value pair in the hash table.

        Args:
            key (K): The key to insert or update.
            value (V): The value to associate with the key.
        """
        hash_index = self._hash_function(key)
        bucket = self.table[hash_index]

        # Update existing key
        for item in bucket:
            if item.key == key:
                item.value = value
                return

        # Insert new key
        bucket.append(HashItem(key, value))

    def get(self, key: K) -> V:
        """Retrieves the value associated with a given key.

        Args:
            key (K): The key to look up.

        Returns:
            V: The associated value.

        Raises:
            KeyError: If the key does not exist in the hash table.
        """
        hash_index = self._hash_function(key)
        bucket = self.table[hash_index]

        for item in bucket:
            if item.key == key:
                return item.value
                
        raise KeyError(f"Key '{key}' not found.")

    def remove(self, key: K) -> None:
        """Removes a key-value pair from the hash table.

        Args:
            key (K): The key to remove.

        Raises:
            KeyError: If the key does not exist in the hash table.
        """
        hash_index = self._hash_function(key)
        bucket = self.table[hash_index]

        for index, item in enumerate(bucket):
            if item.key == key:
                del bucket[index]
                return
                
        raise KeyError(f"Key '{key}' not found.")
