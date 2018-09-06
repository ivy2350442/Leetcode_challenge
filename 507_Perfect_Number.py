class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        s = 0
        r = int(num**0.5)
        for i in range(1, r+1):
            if num % i == 0:
                s += i
                s += int(num/i)

        if r**2 == num :
            s -= r

        return s == 2*num
