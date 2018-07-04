class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        ans = 0

        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    ans = ans + 1

        return ans
