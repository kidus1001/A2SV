# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        emp = {i.id: i for i in employees}

        def dfs(empId):
            employee = emp[empId]
            total = employee.importance
            for x in employee.subordinates:
                total+=dfs(x)
            return total
        return dfs(id)
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        