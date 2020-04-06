# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:33:18 2019

@author: Evan_He
"""

"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: list[Employee]
        :type id: int
        :rtype: int
        """
        res = 0
        id_list = [employee.id for employee in employees]
        index_id = id_list.index(id)
        res += employees[index_id].importance
        subord = employees[index_id].subordinates
        while subord:
            emp = employees[id_list.index(subord.pop())]
            res += emp.importance
            subord += emp.subordinates
        return res