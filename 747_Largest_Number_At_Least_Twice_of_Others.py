class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 0

        l = heapq.nlargest(2, nums)
        if l[0] >= 2 * l[1]:
            return nums.index(l[0])
        return -1
