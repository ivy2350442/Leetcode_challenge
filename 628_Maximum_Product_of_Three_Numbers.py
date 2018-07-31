class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        #排序太慢了
        nums.sort()

        if nums[0] * nums[1] * nums[-1] > nums[-1] * nums[-2] * nums[-3]:
            return nums[0] * nums[1] * nums[-1]
        return nums[-1] * nums[-2] * nums[-3]
        '''

        #透過heap 來找出最大或最小幾個值的執行速度較快
        l = heapq.nlargest(3, nums)
        s = heapq.nsmallest(2, nums)

        if l[0] * l[1] * l[2] > l[0] * s[0] * s[1]:
            return l[0] * l[1] * l[2]
        return l[0] * s[0] * s[1]
