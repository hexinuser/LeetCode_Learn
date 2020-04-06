# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:36:06 2018

@author: Evan_He
"""

class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        if n<3:
            return 0
        else:
            countlist=[]
            t=A[1]-A[0]
            count=0
            for i in range(2,n):
                if A[i]-A[i-1]==t:
                    count+=1
                else:
                    if count>0:
                        countlist.append(count)
                    t=A[i]-A[i-1]
                    count=0
            if count>0:
                countlist.append(count)
        return int(sum([(x**2+x)/2 for x in countlist]))
                    
                    
#方法二 慢
#        import numpy as np
#        def dina(A,k):
#            n=np.size(A)
#            count=0
#            if A[k+1]==A[k]:
#                if k+2<n:
#                    for i in range(k+2,n):
#                        if A[i]!=A[k]:
#                            count=count+ sum(range(i-k))
#                            break
#                        elif i==n-1:
#                            count=count+ sum(range(i-k+1))
#                            break
#                else:
#                    count+=1
#                    i=n-1
#            else:
#                i=k+1
#            return count,i
#        A=np.array(A)
#        B=A[1:]-A[:-1]
#        k=0
#        count=0
#        n=np.size(B)
#        while k<n-1:
#            count1,i=dina(B,k)
#            count+=count1
#            k=i
#        return count
