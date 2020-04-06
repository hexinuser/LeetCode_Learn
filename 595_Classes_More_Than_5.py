# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 13:56:25 2018

@author: Evan_He
"""

# Write your MySQL query statement below

query = '''select class from courses
group by class having count(distinct student)>=5'''