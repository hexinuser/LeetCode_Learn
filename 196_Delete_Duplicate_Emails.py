# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 23:34:02 2018

@author: Evan_He
"""

# Write your MySQL query statement below

query = """DELETE FROM Person WHERE Id NOT IN
(SELECT Id FROM (SELECT MIN(Id) Id FROM Person GROUP BY Email) as p)""" #查询生成的表必须有别名，此处的p


query = """DELETE p1 FROM Person as p1,
    Person as p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id
"""