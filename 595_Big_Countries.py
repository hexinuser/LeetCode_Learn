# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:54:47 2018

@author: Evan_He
"""

# Write your MySQL query statement below
query ="""select name,population,area from World
where area>3000000 or population >25000000"""