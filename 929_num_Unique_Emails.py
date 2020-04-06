# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:18:52 2018

@author: Evan_He
"""

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def email_update(email):
            email_1 = email.split('@')
            local = email_1[0]
            local = local.split('+')[0]
            local = ''.join(local.split('.'))
            return local+'@'+email_1[1]
        unique = set()
        for email in emails:
            unique.add(email_update(email))
        return len(unique)
         