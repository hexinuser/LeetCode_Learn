# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:17:29 2018

@author: Evan_He
"""

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        count=0
        for i in range(len(S)):
            if S[i] in J:
                count+=1
        return count

        '''
        count=0
        for i in range(len(S)):
            for j in range(len(J)):
                if S[i]==J[j]:
                    count+=1
        return count
        '''