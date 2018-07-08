class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans_num = 0
        ans = []
        for i in range(len(ops)):
            if ops[i] == '+':
                temp = ans[-1] + ans[-2]
                ans.append(temp)

            elif ops[i] == 'D':
                temp = ans[-1] + ans[-1]
                ans.append(temp)

            elif ops[i] == 'C':
                ans.pop(len(ans)-1)

            else:
                ans.append(int(ops[i]))

        return sum(ans)
