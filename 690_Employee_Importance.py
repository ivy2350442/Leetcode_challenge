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
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        emp = {emp.id: [emp.importance, emp.subordinates] for emp in employees}
        '''
        emp = {}
        for emplo in employees:
            emp.update({emplo.id: [emplo.importance, emplo.subordinates]})
            #或
            #emp[emplo.id] = [emplo.importance, emplo.subordinates]
        '''

        def importance_value(id):

            if len(emp[id][1]) == 0:
                return emp[id][0]

            else:
                imp = 0
                imp += emp[id][0]

                for i in range(len(emp[id][1])):
                    imp += importance_value(emp[id][1][i])

                return imp

        ans = importance_value(id)
        return ans
