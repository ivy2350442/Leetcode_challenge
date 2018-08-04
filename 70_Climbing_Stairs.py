class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        step = [0, 1, 2]

        for i in range(3, n+1):
            temp = step[i-1] + step[i-2]
            step.append(temp)

        return step[n]
