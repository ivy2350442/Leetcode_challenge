class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        short = min(strs, key=len)
        for i, s in enumerate(short):
            for string in strs:
                if string[i] != s:
                    return short[:i]
        return short
