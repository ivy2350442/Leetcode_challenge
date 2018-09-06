class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        '''
        #執行時間過長
        nums_d = {}
        for i, v in enumerate(nums):
            nums_d[v] = i
        if target in nums_d:
            return nums_d[target]
        else:
            return -1
        '''

        l, r = 0, len(nums) -1
        while l <= r :
            mid = int((r+l)/2)
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
