# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:02:29 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        node = preorder[0]
        res = TreeNode(node)
        index = inorder.index(node)
        res.left = self.buildTree(preorder[1:index+1], inorder[:index])
        res.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return res
        """#利用栈的后进先出，表达子树
        if not preorder:
            return None
        stack=[]#利用栈后进先出的原理
        root=TreeNode(preorder[0])
        stack.append(root)
        index=0
        for i in range(1,len(preorder)):
            cur=stack[-1]
            if(stack[-1].val!=inorder[index]): #表明该中序索引在左子树
                cur.left=TreeNode(preorder[i])
                stack.append(cur.left)
            else:
                while(len(stack)!=0 and stack[-1].val==inorder[index]):
                    cur=stack.pop() #表明该子树一表达完毕
                    index+=1
                if(index<len(inorder)):
                    cur.right=TreeNode(preorder[i])
                    stack.append(cur.right)
        return root
        """