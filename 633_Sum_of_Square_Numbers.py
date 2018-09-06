class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        t = set()
        for i in range(int(c**0.5)+1):
            t.add(i**2)

        for n in t:
            if c-n in t:
                return True
        return False
        
