class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #import math
        #return int(math.sqrt(x))
        """
        if x==0:
            return 0
        for i in range(x+1):
            if (i+1)**2>x:
                break
        return i
        """
        a = 0
        b = x
        if x==0:
            return 0
        while True:
            t = (a+b)//2
            if t**2<=x: 
                if (t+1)**2>x:
                    return t
                else:
                    a = t+1
            else:
                b = t-1
        