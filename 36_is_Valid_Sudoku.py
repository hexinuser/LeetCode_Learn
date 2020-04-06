# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:25:42 2019

@author: Evan_He
"""

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if len(set(row)) + row.count('.')!= 10:
                return False
        for col in zip(*board):
            if len(set(col)) + col.count('.')!= 10:
                return False
        for i in [0,3,6]:
            for j in [0,3,6]:
                squ = board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3]
                if len(set(squ)) + squ.count('.')!= 10:
                    return False
        return True