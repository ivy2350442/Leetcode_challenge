class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0
        for i in range(len(s)):
            #'**' 表示平方
            ans += (ord(s[len(s)-1-i])-64) * (26**i)

        return ans
