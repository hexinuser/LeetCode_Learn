# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 19:15:04 2018

@author: Evan_He
"""

query = """select Name Customers from Customers
where Customers.id not in
(select Customerid from Orders) """

query = """ select Name as Customers from Customers left join Orders on Customers.Id = Orders.CustomersId where Orders.CustomerId is null"""