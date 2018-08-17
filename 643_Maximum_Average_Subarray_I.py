class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        ave = sum(nums[:k])
        ans = ave
        for i in range(len(nums)-k):
            ave = ave - nums[i] + nums[i+k]
            if ave > ans:
                ans = ave

        return ans/float(k)
