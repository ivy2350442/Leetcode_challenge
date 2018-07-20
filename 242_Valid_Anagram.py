class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        if set(s) != set(t):
            return False

        count_s = collections.Counter(s)
        count_t = collections.Counter(t)

        for word in count_s:
            if count_s[word] != count_t[word]:
                return False
        return True
