# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:33:15 2018

@author: Evan_He
"""
# Write your MySQL query statement below
query = """select Email from 
(select Email,count(Email) as num from Person group by Email) as p 
where num > 1"""

query_1 = """select Email
from Person
group by Email
having count(Email) > 1;"""