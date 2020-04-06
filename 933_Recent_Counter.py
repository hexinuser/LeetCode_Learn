# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:45:54 2019

@author: Evan_He
"""
import collections
class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()
        #双向队列

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)