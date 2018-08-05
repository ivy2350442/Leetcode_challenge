class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        ans = []
        c = ''
        index = -1
        for i in range(len(S)):
            if S[i] != c:
                if i - index > 2:
                    ans.append([index, i-1])
                index = i
                c = S[i]

            #判斷最後的連續字串問題
            if i == len(S)-1:
                if i - index >= 2:
                    ans.append([index, i])

        return ans
