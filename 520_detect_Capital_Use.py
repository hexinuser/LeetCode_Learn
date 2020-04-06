# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 22:35:49 2018

@author: Evan_He
"""

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.istitle() or word.islower() or word.isupper()
        """ 
        if word.title()==word:
            return True
        elif word.upper()==word:
            return True
        elif word.lower()==word:
            return True
        else:
            return False
        """