class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        ans = ''
        length = len(S) - 1
        k = 0
        while length != -1:
            if S[length] != '-':
                ans = S[length].upper() + ans
                k += 1

                if k == K:
                    ans = '-' + ans
                    k = 0
            length -= 1

        if ans == '':
            return ''

        if ans[0] == '-':
            return ans[1:]

        return ans
