class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        #采用递归形式计算
        if num==0:
            return 'Zero'
        ones = ['One', 'Two', 'Three', 'Four', 'Five', 'Six',
                'Seven', 'Eight', 'Nine']
        tens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                 'Fifteen', 'Sixteen','Seventeen','Eighteen','Nineteen']
        hundreds = ['Twenty', 'Thirty', 'Forty','Fifty',
                    'Sixty','Seventy', 'Eighty', 'Ninety']
        result=''
        if num<10**3:
            if num >=100:
                t = num//100
                result += ones[t-1]+' Hundred '
                num = num%100
            if num >=20:
                t = num//10
                result += hundreds[t-2]+' '
                num = num%10
                if num !=0:
                    result +=ones[num-1]
                return result.rstrip()
            if num >=10:
                t = num -10
                result += tens[t]
            else:
                if num!=0:
                    result += ones[num-1]
            return result.rstrip()
        if num<(10**6):
            t = num//(10**3)
            result += self.numberToWords(t)+' Thousand'
            num = num%(10**3)
            if num == 0:
                return result
            else:
                result += ' '+self.numberToWords(num)
                return result
        if num<(10**9):
            t = num//(10**6)
            result += self.numberToWords(t)+' Million'
            num = num%(10**6)
            if num == 0:
                return result
            else:
                result += ' '+self.numberToWords(num)
                return result
        else:
            t = num//(10**9)
            result += self.numberToWords(t)+' Billion'
            num = num%(10**9)
            if num == 0:
                return result
            else:
                result += ' '+self.numberToWords(num)
                return result


            
                
            
                   
            