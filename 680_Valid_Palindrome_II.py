class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s_b = s[::-1]

        if s == s_b:
            return True

        for i in range(len(s)):
            if s[i] != s_b[i]:

                s_n = s[:i] + s[i+1:]
                s_b_n = s_n[::-1]

                s = s[:len(s)-1-i] + s[len(s)-i:]
                s_b = s[::-1]
                break

        return s_n == s_b_n or s == s_b
