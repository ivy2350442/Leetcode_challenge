class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        num = bin(num)[2:]
        comp = ' '
        for i in range(len(num)):
            if num[len(num) - i - 1] == '0':
                comp = '1' + comp
            else:
                comp = '0' + comp

        ans = int(comp,2)
        return ans
