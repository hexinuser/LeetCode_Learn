# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:00:41 2018

@author: Evan_He
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """#方法一，利用动态规划查找S和S[::-1]的最大公共子串，需要检查子串的索引是否与反向子串的原始索引相同
            # 时间复杂度和空间复杂度都是O(n^2)
                n = len(s)
        s1 = s[::-1]
        if s==s1:
            return s
        tree = []
        res = [0,0]
        for i in range(n):
            tree_sub = [0 for _ in range(n)]
            for j in range(n):
                if s[i]==s1[j]:
                    if i==0 or j ==0:
                        tree_sub[j] = 1
                    else:
                        tree_sub[j] = tree[i-1][j-1]+1
                if tree_sub[j]>=res[0]:
                    if j!=i or (i==j and 2*i-tree_sub[j]==n-2):
                        res = [tree_sub[j],i]
            tree.append(tree_sub)
        return s[res[1]-res[0]+1:res[1]+1]
        
        """
        """#方法二，暴力法，遍历所有子串是否为回文串，修正，防止重复验证 
        n = len(s)
        if s==s[::-1]:
            return s
        res = s[0]
        lens = 1
        for i in range(n):
            j = i+lens+1
            if j>n:
                return res
            while j<=n:
                if s[i:j]==s[i:j][::-1]:
                    res = s[i:j]
                    lens = j-i
                j += 1
        return res
        """
        """ #解法三: 动态规划方法,中心点到两边
        n = len(s)
        if n <= 1:
            return s
        max_length = 0 #存储左右两端长度
        res = ''
        for i in range(n):
            x = 1
            while (i-x) >= 0 and (i+x) < n:
                if s[i+x] == s[i-x]:  #以i为中心
                    x += 1
                else:
                    break
            x -= 1 
            if 2*x+1 > max_length:
                max_length = 2*x + 1
                res = s[i-x: i+x+1]
            x = 0
            if (i + 1) < n:
                while (i - x) >= 0 and (i + 1 + x) < n: #二字母回文
                    if s[i+1+x] == s[i- x]:
                        x += 1
                    else:
                        break
            x -= 1
            if 2 * x + 2 > max_length:
                max_length = 2 * x + 2
                res = s[i-x: i+x+2]
                
        if res == '':
            res = s[0]
        return res
        """
        """#解法四：Manacher 算法 https://www.felix021.com/blog/read.php?2040
        T = '#'+'#'.join(s)+'#'
        n = len(T)
        P = [1 for _ in range(n)]
        max_num = 0
        mid = 0
        bound = 0
        i = 0
        while i <n:
            if bound>i:         
#                if bound-i>P[2*mid-i]:
#                    P[i] = P[2*mid-i]   
#                else:
#                    P[i] = bound-i             
                P[i] = min(bound-i,P[2*mid-i])
            while i-P[i]>=0 and i+P[i]<n:
                if T[i-P[i]] == T[i+P[i]]:
                    P[i] +=1
                else:
                    break
            if i+P[i]>bound:
                mid = i
                bound = i+P[i]
            if P[i]>max_num:
                max_num =P[i]    
            i += 1
        max_index = P.index(max_num)
        res = T[max_index-max_num+1:max_index+max_num]
        return res.replace('#','')
        """
        
        #解法五，算法四的变形
        n = len(s)
        s_inv = s[::-1]
        lens = 0 #初始为偶数个
        start = 0
        for i in range(n):
            if i - lens >= 1 and s[i - lens - 1: i + 1] == s_inv[n-i-1:n+1+lens-i]: #回文长度为2+lens，长度偶数个增加，直接增加i，反之考虑个数增加奇数个
                start = i - lens - 1
                lens += 2
                continue
            if i - lens >= 0 and s[i - lens: i + 1] == s_inv[n-i-1:n+lens-i]: #考虑以i为中心
                start = i - lens
                lens += 1
        return s[start: start + lens]
        
        
        
        
        
        
        
        





def commonSubstring(S1,S2):
    """ 利用动态规划方法求最大公共子串
        详见 https://en.wikipedia.org/wiki/Longest_common_substring_problem    
    """
    m = len(S1)
    n = len(S2)
    tree = []
    res = [0,0]
    for i in range(m):
        tree_sub = [0 for _ in range(n)]
        for j in range(n):
            if S1[i]==S2[j]:
                if i==0 or j ==0:
                    tree_sub[j] = 1
                else:
                    tree_sub[j] = tree[i-1][j-1]+1
                if tree_sub[j]>res[0]:
                    res = [tree_sub[j],i]
        tree.append(tree_sub)
    return tree
                

                