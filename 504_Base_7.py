class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        ans = ''
        n = ''
        if num < 0:
            n = '-'
            num = -1 * num

        while num >= 7:
            ans = str(num % 7) + ans
            num = int(num/7)

        ans = n + str(num) + ans
        return ans
        
