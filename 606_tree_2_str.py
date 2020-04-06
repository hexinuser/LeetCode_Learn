# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:08:41 2018

@author: Evan_He
"""

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        res = str(t.val)
        if not t.left and not t.right:
            return res
        if t.left:
            res += '(%s)'%self.tree2str(t.left)
        else:
            res += '()'
        if t.right:
            res += '(%s)'%self.tree2str(t.right)
        return res