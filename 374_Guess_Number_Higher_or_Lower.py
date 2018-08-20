# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        h, l = 0, 0
        while guess(n) != 0:
            if guess(n) == -1:
                h = n
                n = (l + n) // 2
            else:
                l = n
                n = (n + h) // 2

        return n
