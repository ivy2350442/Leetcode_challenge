class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]

        ans = [1, 1]
        for i in range(1, rowIndex):
            temp = []
            temp.append(1)

            for j in range(i):
                temp.append(ans[j] + ans[j+1])
            temp.append(1)
            ans = temp

        return ans
