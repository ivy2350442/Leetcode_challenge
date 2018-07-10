class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        #為避免一開始無法進入for迴圈 因此必須要給一個空字串
        ans = ['']

        for i in S:
            if i.isalpha():
                temp = []
                for c in ans:
                    temp.append(c + i.lower())
                    temp.append(c + i.upper())
                #等號將可避免因出 a, A, ab, aB, ... 問題
                ans = temp

            else:
                temp = []
                for c in ans:
                    temp.append(c + i)
                ans = temp

        return ans
