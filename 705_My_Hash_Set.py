# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 09:43:39 2018

@author: Evan_He
"""

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = set()

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.hash.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.hash:
            self.hash.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.hash
    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)