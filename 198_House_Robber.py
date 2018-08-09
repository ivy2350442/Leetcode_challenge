class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m, c = 0, 0

        for num in nums:
            m, c = c, max(c, m + num)

        return max(m, c)
