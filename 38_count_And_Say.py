class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """      
        def count_num(tn):
            n = len(tn)
            tn_next = ''
            count = 1
            for i in range(1,n):
                if tn[i-1]==tn[i]:
                    count+=1
                    if i == n-1:
                        tn_next +=str(count)+tn[i]  
                
                else:
                    tn_next += str(count)+tn[i-1]
                    count = 1
                    if i == n-1:
                        tn_next +=str(count)+tn[i]  
            return tn_next
                
        if n==1:
            return '1'
        elif n==2:
            return '11'
        else:
            tn='11'
            k=2
            while k<n:
                tn=count_num(tn)
                k+=1
        return tn
        """ #利用正则化模块进行匹配
        import re
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(p[0])) + p[1] for p in re.findall('((.)\\2*)', s))
            #\\2表示第二场括号匹配内容相同，同样\\3
            #s = ''.join(str(len(p[0])) + p[1] for p in re.findall(r'((.)\2*)', s)) #加r表示匹配原生字符串
        return s
        """