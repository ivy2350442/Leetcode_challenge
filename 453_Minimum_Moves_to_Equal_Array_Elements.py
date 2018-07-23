class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # sum + 移動次數M * (len(list)N - 1) = 最後得到的相等數X * N
        # X = minNum + M
        #兩式做聯立方程式解

        return sum(nums) - min(nums) * len(nums)
