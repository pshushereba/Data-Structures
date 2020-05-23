import sys
sys.path.append('/doubly_linked_list.py')
from doubly_linked_list import *

from collections import OrderedDict

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.length = limit
        self.storage = DoublyLinkedList()
        self.cache_order = OrderedDict()


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Look up value by key
        if key not in self.cache_order:
            return None
        #node = self.cache_order[key]
        node = ListNode(self.cache_order[key]) # add to dictionary; don't use ListNode
        # move node to head of list
        # node.add_to_head()
    

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if self.length == 10:
            self.storage.remove_from_tail()
        else:
            self.storage.add_to_head(value)
            self.cache_order[key] = value
            # increase length of list
        print(self.cache_order)

        # check length of list
        # remove tail if list is full
        # 