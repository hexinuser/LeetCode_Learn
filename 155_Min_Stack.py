# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 23:19:52 2018

@author: Evan_He
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []
        self.__min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.__stack.append(x)
        if self.__min == None or self.__min > x:
            self.__min = x

    def pop(self):
        """
        :rtype: void
        """
        t = self.__stack.pop()
        if t == self.__min:
            if self.__stack:
                self.__min = min(self.__stack)
            else:
                self.__min = None
        
    def top(self):
        """
        :rtype: int
        """
        return self.__stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.__min
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
