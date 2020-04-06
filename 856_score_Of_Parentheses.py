# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:46:30 2018

@author: Evan_He
"""

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        """#递归思想
        def count_sub(num_s):
            if not num_s:
                return 0
            if len(num_s) == 2:
                return 1
            j = num_s[1:].index(num_s[0])+1
            if j == 1:
                return 1 + count_sub(num_s[2:])
            else:
                return 2*count_sub(num_s[1:j]) + count_sub(num_s[j+1:])
        new_s,k = [],1
        for s in S:
            if s == '(':
                new_s.append(k)
                k += 1
            else:
                new_s.append(k-1)
                k -= 1
        return count_sub(new_s)
        """
        #栈
        stack = []
        for s in S:
            if s=='(':
                stack.append(s)
            else:
                score = 0
                while stack:
                    t = stack.pop()
                    if t=='(':
                        if score==0:
                            stack.append(1)
                        else:
                            stack.append(score*2)
                        break
                    else:
                        score += t
                    if not stack:
                        return score
        return sum(stack)
        
                
        