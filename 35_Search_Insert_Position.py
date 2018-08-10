class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target > nums[-1]:
            return len(nums)

        if target < nums[0]:
            return 0

        i, c = 0, 0
        while i != len(nums):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
            i += 1
