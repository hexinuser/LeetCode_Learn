# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:47:55 2018

@author: Evan_He
"""

# Write your MySQL query statement below

query = """select p1.Name as Employee
from Employee as p1 inner join Employee as p2
on p1.ManagerId = p2.Id
where p1.Salary > p2.Salary""" 