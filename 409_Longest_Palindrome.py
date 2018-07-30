class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = collections.Counter(s)

        ans = 0
        odd = 0

        for v in count.values():
            ans += int(v/2) * 2

        if ans != len(s):
            ans += 1

        return ans
