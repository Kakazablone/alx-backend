#!/usr/bin/env python3
"""BasicCache is a caching system that inherits from BaseCaching.
This class implements a basic cache with no size limit. Items are stored
in a dictionary and can be retrieved by their keys. If a key or item is
None, the put method will do nothing. The get method will return the
associated value for a given key or None if the key doesn't exist.
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):

    def put(self, key, item):
        """Add an item to the cache.

        If key or item is None, the method does nothing.

        Args:
            key: The key associated with the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by its key.

        If key is None or doesn't exist in the cache, None is returned.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The item associated with the key, or None if the key doesn't exist.
        """
        return self.cache_data.get(key)
