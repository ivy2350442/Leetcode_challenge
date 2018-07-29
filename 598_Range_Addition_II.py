class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """

        if ops == []:
            return m*n

        ops0 = []
        ops1 = []
        for op in ops:
            ops0.append(op[0])
            ops1.append(op[1])

        return min(ops0) * min(ops1)
