#!/usr/bin/env python3
"""
FIFOCache Module
"""
from collections import OrderedDict
BaseCache = __import__("0-basic_cache").BasicCache


class FIFOCache(BaseCache):
    """
    A Subclass of BasicCache
    """

    def __init__(self):
        """
            self: Object to be created
        """
        super().__init__()

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
        len_cache = len(self.cache_data)
        if len_cache < BaseCache.MAX_ITEMS:
            self.cache_data[key] = item
        else:
            self.cache_data = OrderedDict(self.cache_data)
            removed_key, removed_value = self.cache_data.popitem(last=False)
            print("Discard: {:s}".format(removed_key))
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
