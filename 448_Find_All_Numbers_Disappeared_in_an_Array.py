class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # set(數字的序列) 會排序由小到大
        nums_set = set(nums)

        ans = []
        for iters in range(1, len(nums) + 1, 1):
            if iters not in nums_set:
                ans.append(iters)

        return ans
