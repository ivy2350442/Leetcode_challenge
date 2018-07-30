class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        #太慢了
        nums.sort()
        for ind, v in enumerate(nums):
            if ind != v:
                return ind

        return len(nums)
        '''

        length = len(nums)
        num_sum = (length+1) * length / 2
        return int(num_sum) - sum(nums)
