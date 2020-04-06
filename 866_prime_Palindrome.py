class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def judge_pri(n):
            if (n+1)%6!=0 and (n-1)%6!=0:
                return False
            left,right = 2,n//2
            while left <=right:
                if n%left == 0:
                    return False
                else:
                    left += 1
                    right = n//left
            return True
        def find_pal(num):
            res = str(num)
            n = len(res)//2
            if res[n-1::-1] >= res[n+1:]:
                return int(res[:n+1]+res[n-1::-1])
            else:
                if res[n]!='9':
                    t = str(int(res[n])+1)
                    return int(res[:n]+t+res[n-1::-1])
                else:
                    a = str(int(res[:n])+1)
                    if len(a)>n:
                        return 10*(2*n+1)+1
                    else:
                        return int(a+'0'+a[::-1])
        if N == 1:
            return 2
        elif N < 4:
            return N
        elif N<6:
            return 5
        elif N<8:
            return 7
        elif N<12:
            return 11
        K = len(str(N))
        if K%2==0:
            return self.primePalindrome(10**K+1)
        else:
            res = find_pal(N)
            if judge_pri(res):
                return res
            else:
                return self.primePalindrome(res+1)
                
        
        