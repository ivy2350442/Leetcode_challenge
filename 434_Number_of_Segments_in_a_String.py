class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.split( )
        ans = 0
        for i in s:
            if i != ' ':
                ans += 1

        return ans
