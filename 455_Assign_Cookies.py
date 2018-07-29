class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        if len(g) == 0 or len(s) == 0:
            return 0

        g.sort()
        s.sort()

        ans = 0
        p = 0
        for i in g:
            while (i > s[p]):
                p += 1
                if p == len(s):
                    break
            if p == len(s):
                    break
            ans += 1
            p += 1
            if p == len(s):
                    break

        return ans
