class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        s = ''
        count = 0
        while len(s) <= len(B):
            s += A
            count += 1
            if B in s:
                return count

        s += A
        if B in s:
            return count + 1

        return -1
