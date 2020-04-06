# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:34:57 2018

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 两两合并，归并排序
        def mergeNode(node1,node2):
            if not node1:
                return node2
            if not node2:
                return node1
            if node1.val < node2.val:
                res = ListNode(node1.val)
                res.next = mergeNode(node1.next,node2)
                return res
            else:
                res = ListNode(node2.val)
                res.next = mergeNode(node1,node2.next)
                return res
            
        if lists == []:
            return None
        n = len(lists)
        if n == 1:
            return lists[0]
        res = []
        for i in range(0,n-1,2):
            res.append(mergeNode(lists[i],lists[i+1]))
        if n % 2 == 1:
            res.append(lists[-1])
        return self.mergeKLists(res)

            
        
        
        """ k个直接排序，超时
        import math
        if m == 0:
            list1 = []
            for i in range(len(lists)):
                if lists[i]!=None:
                    list1.append(lists[i])
            lists = list1
        if len(lists) == 0:
            return None        
        if len(lists) == 1:
            return lists[0]
        else:
            min_t = math.inf
            k= -1
            for i in range(len(lists)):
                if min_t>lists[i].val:
                    min_t = lists[i].val
                    k = i
            result = ListNode(min_t)
            if lists[k].next == None:
                del lists[k]
            else:
                lists[k] = lists[k].next
            result.next = self.mergeKLists(lists,1)
            return result
        """
            