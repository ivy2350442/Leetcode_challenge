class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        ans = []
        for h in range(12):
            for m in range(60):
                if bin(h)[2:].count('1') + bin(m)[2:].count('1') == num:
                    ans.append('%d:%02d' % (h, m))

        return ans
