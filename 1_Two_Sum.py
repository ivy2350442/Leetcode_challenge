class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [nums.index(target - nums[i]), i]
            else:
                dic[nums[i]] = i
        