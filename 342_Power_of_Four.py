class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #n = abs(num)

        if num == 0:
            return False
        if num == 1:
            return True

        while num != 4:
            if (num % 4) != 0:
                return False
            num = num / 4
        return True
