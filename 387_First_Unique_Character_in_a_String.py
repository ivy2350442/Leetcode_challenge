class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return -1

        counter = collections.Counter(s)

        count = 0
        ans = len(s)
        for k in counter:
            if counter[k] == 1:
                if s.index(k) < ans:
                    ans = s.index(k)
            else:
                count += 1

        if count == len(set(s)):
            return -1

        return ans
