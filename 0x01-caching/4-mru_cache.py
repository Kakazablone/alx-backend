#!/usr/bin/env python3
""" Function that implements the Most
Recently used caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache is a caching system that inherits from BaseCaching.

    This class implements an MRU (Most Recently Used) caching system.
    When the cache exceeds its maximum capacity, the most recently used
    item is discarded.
    """

    def __init__(self):
        """Initialize the MRUCache."""
        super().__init__()
        self.most_recent_key = None  # Track the most recently used key

    def put(self, key, item):
        """Add an item to the cache using the MRU strategy.

        If the cache exceeds its maximum size, the most recently used item
        is removed.

        Args:
            key: The key associated with the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.most_recent_key is not None:
                    del self.cache_data[self.most_recent_key]
                    print(f"DISCARD: {self.most_recent_key}")

            self.cache_data[key] = item
            self.most_recent_key = key
            # Update the most recent key to the current one

    def get(self, key):
        """Retrieve an item from the cache by its key.

        If the key exists, it will be marked as the most recently used.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The item associated with the key, or None if the key doesn't exist.
        """
        if key is not None and key in self.cache_data:
            # Update the most recent key to the accessed key
            self.most_recent_key = key
            return self.cache_data[key]
        return None
