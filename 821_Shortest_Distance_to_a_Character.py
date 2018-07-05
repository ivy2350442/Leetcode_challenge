class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        ans = []
        for i in range(len(S)):
            temp = 0
            for j in range(len(S)):
                if i+j >= len(S):
                    if S[i-j] == C or i-j < 0:
                        break
                    else:
                        temp = temp + 1
                elif S[i+j] == C or S[i-j] == C and i-j >= 0:
                    break
                else:
                    temp = temp + 1
            ans.append(temp)

        return ans
