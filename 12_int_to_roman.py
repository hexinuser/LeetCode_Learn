# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:44:41 2018

@author: Evan_He
"""

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strs = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX",
                "V", "IV", "I"]
        i=0
        result = ''
        while num!=0:
            if num>=num_list[i]:
                num-=num_list[i]
                result+=strs[i]
            else:
                i+=1
        return result
        
        
        
        """
        result=''
        t4=num//1000
        if t4!=0:
            result +='M'*t4
            num-=1000*t4
        if num-900>=0:
            result +='CM'
            num-=900
            if num-90>=0:
                result +='XC'
                num-=90
            elif num-50>=0:
                result +='L'
                num-=50
            elif num-40>=0:
                result +='XL'
                num-=40
            
            t=num//10
            if t!=0:
                result +='X'*t
                num-=10*t
            if num-9==0:
                result +='IX'
                return result
            elif num-5>=0:
                result +='V'
                num-=5
            elif num-4>=0:
                result +='IV'
                return result
            result+='I'*num
        elif num-500>=0:
            result +='D'
            num-=500
            t=num//100
            if t!=0:
                result+='C'*t
                num-=100*t
            if num-90>=0:
                result +='XC'
                num-=90
            elif num-50>=0:
                result +='L'
                num-=50
            elif num-40>=0:
                result +='XL'
                num-=40
            
            t=num//10
            if t!=0:
                result +='X'*t
                num-=10*t
            if num-9==0:
                result +='IX'
                return result
            elif num-5>=0:
                result +='V'
                num-=5
            elif num-4>=0:
                result +='IV'
                return result
            result+='I'*num
        elif num-400>=0:
            result +='CD'
            num-=400
            if num-90>=0:
                result +='XC'
                num-=90
            elif num-50>=0:
                result +='L'
                num-=50
            elif num-40>=0:
                result +='XL'
                num-=40
            
            t=num//10
            if t!=0:
                result +='X'*t
                num-=10*t
            if num-9==0:
                result +='IX'
                return result
            elif num-5>=0:
                result +='V'
                num-=5
            elif num-4>=0:
                result +='IV'
                return result
            result+='I'*num   
        else:
            t=num//100
            if t!=0:
                result +='C'*t
                num-=100*t
            if num-90>=0:
                result +='XC'
                num-=90
            elif num-50>=0:
                result +='L'
                num-=50
            elif num-40>=0:
                result +='XL'
                num-=40
            
            t=num//10
            if t!=0:
                result +='X'*t
                num-=10*t
            if num-9==0:
                result +='IX'
                return result
            elif num-5>=0:
                result +='V'
                num-=5
            elif num-4>=0:
                result +='IV'
                return result
            result+='I'*num              
        return result
        """
     