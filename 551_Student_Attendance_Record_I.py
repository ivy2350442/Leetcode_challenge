class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s.count('A') < 2 and 'LLL' not in s:
            return True

        return False
