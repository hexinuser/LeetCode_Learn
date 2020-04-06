class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m,n = len(a),len(b)
        if m <n:
            m,n,a,b = n,m,b,a
        a = [x for x in a]
        add = False
        for i in range(1,m+1):
            if i<=n:
                if add:
                    if a[-i] == '1':
                        if a[-i]!=b[-i]:
                            a[-i]='0'
                    else:
                        if a[-i]==b[-i]:
                            a[-i]='1'  
                            add = False
                else:
                    if a[-i] == '1':
                        if a[-i]==b[-i]:
                            a[-i]='0'
                            add = True
                    else:
                        if a[-i]!=b[-i]:
                            a[-i]='1'  
            else:
                if add:
                    if a[-i]=='1':
                        a[-i]='0'
                    else:
                        a[-i]='1'
                        return ''.join(a)
                else:
                    return ''.join(a)
        if add:
            return '1'+''.join(a)
        else:
            return ''.join(a)
                