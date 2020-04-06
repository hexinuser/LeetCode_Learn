# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:31:39 2018

@author: Evan_He
"""

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = []
        dict_domain = {}
        for cpdomain in cpdomains:
            domain = cpdomain.split()
            num = int(domain[0])
            list_domain = domain[1].split('.')
            for i in range(len(list_domain)):
                dom = '.'.join(list_domain[i:])
                if dom in dict_domain:
                    dict_domain[dom] += num
                else:
                    dict_domain[dom] = num
        for key,value in dict_domain.items():
            res.append(str(value)+' '+key)
        return res