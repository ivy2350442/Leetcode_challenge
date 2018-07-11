class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        ans = str(num)
        while (len(ans) != 1):
            temp = []
            for i in ans:
                temp.append(int(i))
            ans = str(sum(temp))

        return int(ans)
