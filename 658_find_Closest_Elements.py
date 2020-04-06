# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:05:39 2019

@author: Evan_He
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        arr0 = arr[:]
        res = 0
        for i in range(k):
            arr0[i] = abs(arr0[i]-x)
        for j in range(k,len(arr0)):
            if arr0[j] <= x:
                arr0[j] = x - arr0[j]
                res += 1
            else:
                arr0[j] -= x
                if arr0[j] < arr0[res]:
                    res += 1
                else:
                    break
        return arr[res:res+k]
        """
        def find_mid(arr0,x):
            i,j = 0,len(arr0)
            while i<j:
                mid = (i+j)//2
                if arr0[mid] == x:
                    return mid
                elif arr0[mid] < x:
                    if arr0[mid-1] >= x:
                        return mid
                    else:
                        i = mid+1
                else:
                    if arr0[mid-1] <= x:
                        return mid-1
                    else:
                        j = mid-1
            return mid
        mid = find_mid(arr,x)
        begin = max(0,mid-k+1)
        end = min(len(arr),mid+k)
        res = arr[begin:end]
        num = 0
        for i in range(k):
            res[i] = x - res[i]
        for j in range(k,len(res)):
            res[j] -= x
            if res[j] < res[num]:
                    num += 1
            else:
                break
        return arr[begin+num:begin+num+k]
    
        """
        i,j = 0,len(arr)-k
        if j == 0:
            return arr
        while i < j:
            mid = (i+j)//2
            if abs(arr[mid]-x) <= abs(arr[mid+k]-x) and arr[mid+k]>x:
                j = mid
            else:
                i = mid+1 
        return arr[i:i+k]
        """
                    
                    
                    
                    
                    
                    
                    
                    
                    