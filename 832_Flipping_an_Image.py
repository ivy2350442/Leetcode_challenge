class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        ans = []
        for i in range(len(A)):
            length = len(A[i])
            temp_list = []
            for j in range(length):
                temp = length - j - 1
                if A[i][temp] == 0:
                    temp_list.append(1)
                else:
                    temp_list.append(0)
            ans.append(temp_list)

        return ans
