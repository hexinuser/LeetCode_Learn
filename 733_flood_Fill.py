# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:52:36 2019

@author: Evan_He
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        m, n = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        mod_set = set()
        change = [(sr,sc)]
        while change:
            (a,b) = change.pop()
            mod_set.add((a,b))
            if image[a][b] == color:
                image[a][b] = newColor
                if a >= 1:
                    if (a-1,b) not in mod_set:
                        change.append((a-1,b))
                if a+1 < m:
                    if (a+1,b) not in mod_set:
                        change.append((a+1,b))
                if b >= 1:
                    if (a,b-1) not in mod_set:
                        change.append((a,b-1))
                if b+1 < n:
                    if (a,b+1) not in mod_set:
                        change.append((a,b+1))
        return image
    
"""
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
"""