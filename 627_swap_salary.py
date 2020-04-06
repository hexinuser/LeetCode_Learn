# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:38:24 2018

@author: Evan_He
"""

# Write your MySQL query statement below
query = '''UPDATE salary SET sex  = (CASE sex WHEN 'm' THEN 'f' ELSE 'm' END)'''