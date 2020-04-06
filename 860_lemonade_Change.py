# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:33:27 2019

@author: Evan_He
"""

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count_money = [0,0]
        for bill in bills:
            if bill == 5:
                count_money[0] += 1
            elif bill == 10:
                count_money[0] -= 1
                count_money[1] += 1
            else:
                if count_money[1] > 0:
                    count_money[1] -= 1
                    count_money[0] -= 1
                else:
                    count_money[0] -= 3
            if count_money[0] < 0 or count_money[1] < 0:
                return False
        return True