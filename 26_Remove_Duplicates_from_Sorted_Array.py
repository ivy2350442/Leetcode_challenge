class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        h = 0
        for i in range(1, len(nums)):
            if nums[h] != nums[i]:
                h += 1
                nums[h] = nums[i]

        return h+1
