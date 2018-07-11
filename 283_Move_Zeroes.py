class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        '''
        #遇到不是0 就跟前面的0對調位置
        zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        '''

        length = len(nums)
        count = 0
        index = 0
        while (count != length):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                count += 1

            else:
                index += 1
                count += 1
