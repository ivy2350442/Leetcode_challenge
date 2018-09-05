class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        max_list = heapq.nlargest(3, nums)
        if len(max_list) < 3:
            return max_list[0]
        else:
            return max_list[-1]
