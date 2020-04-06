# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:54:31 2019

@author: Evan_He
"""

class Solution:

    def __init__(self, nums: List[int]):
        self.init = nums.copy()
        self.nums = nums
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.init
    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()