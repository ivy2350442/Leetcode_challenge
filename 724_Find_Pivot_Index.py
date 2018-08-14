class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        h, l = 0, sum(nums)

        for i in range(len(nums)):
            l -= nums[i]
            if h == l:
                return i
            h += nums[i]

        return -1
