# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:05:37 2018

@author: Evan_He
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        num = 1
        for i in range(1,n+1):
            if num==1:
                t = digits[-i]+1
                if t<10:
                    digits[-i] = t
                    return digits
                else:
                    digits[-i] = t-10
        return [1]+digits
        
        
        """
        n = len(digits)
        digit = [digits[i]*10**(n-1-i) for i in range(n)]
        digit = sum(digit)+1
        result = []
        while digit>=10:
            result.append(digit%10)
            digit = digit//10
        result.append(digit)
        return result[::-1]
        """
        """
        n = len(digits)
        digits[n - 1] += 1
        for i in range(n - 1, 0, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i - 1] += 1
        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits
        return digits
        """