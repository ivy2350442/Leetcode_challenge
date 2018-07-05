class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """

        line = 1
        unit = 0

        for i in range(len(S)):
            letter = ord(S[i]) - 97
            if unit + widths[letter] > 100:
                line = line + 1
                unit = 0
            unit = unit + widths[letter]

        ans = []
        ans.append(line)
        ans.append(unit)

        return ans
