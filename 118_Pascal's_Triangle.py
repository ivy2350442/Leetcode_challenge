class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ans = []
        for i in range(1 ,numRows+1):
            temp = []
            if i == 1:
                temp.append(1)
            else:
                for j in range(i):
                    if j == 0:
                        temp.append(1)
                    elif j == i-1:
                        temp.append(1)
                    else:
                        temp.append(ans[i-2][j-1] + ans[i-2][j])
            ans.append(temp)

        return ans
