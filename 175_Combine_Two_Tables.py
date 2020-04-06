# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:17:40 2018

@author: Evan_He
"""

# Write your MySQL query statement below

query = """select FirstName, LastName, City, State
from Person left join Address
on Address.PersonId = Person.PersonId"""