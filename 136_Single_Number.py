class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_set = set()
        for i in range(len(nums)):
            # if _ in set(_) runtime比較快
            # if 判斷可以用 not in
            if nums[i] not in nums_set:
                nums_set.add(nums[i])
            else:
                nums_set.remove(nums[i])
        return nums_set.pop()
