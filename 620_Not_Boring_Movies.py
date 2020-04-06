# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:16:55 2018

@author: Evan_He
"""
# Write your MySQL query statement below
query ="""select * from cinema
where mod(id,2) = 1 and description != 'boring'
order by rating desc"""