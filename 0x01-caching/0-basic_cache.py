#!/usr/bin/env python3
"""
Basic cache Model
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A Subclass of BaseCache
    """
    def put(self, key: str, item: str) -> None:
        """
        Add an item in the cache

        Arguments:
                key(str): Key pair of the dictionary
                item(str): Value to store to a pair of key
        Return:
                None or the value of the key obtain
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: str) -> str:
        """
        Get an item by key
        Arguments:
                key(str): Key pair of the dictionary
        Return:
               Stored value of the or None
        """
        return self.cache_data.get(key, None)
