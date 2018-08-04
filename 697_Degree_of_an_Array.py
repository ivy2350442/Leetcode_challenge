class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = collections.Counter(nums)
        count_max = max(count.values())

        #關鍵影響時間的判斷式
        if count_max == 1:
            return 1

        nums_i = nums[::-1]

        ans = len(nums)
        for i in count:
            if count[i] == count_max:
                f = nums.index(i)
                l = len(nums) - nums_i.index(i)
                if ans > l - f:
                    ans = l - f

        return ans
