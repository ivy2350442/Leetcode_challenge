class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        c = m = nums[0]
        for n in nums[1:]:
            c = max(n, c+n)
            m = max(m, c)

        return m
