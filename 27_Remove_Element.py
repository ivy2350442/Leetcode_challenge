class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        try:
            while True:
                nums.remove(val)

        except:
            #當try 發生error 表示nums 中已不存在val
            return len(nums)

        '''
        #執行速度太慢
        i = len(nums) - 1
        while i != -1:
            if nums[i] == val:
                nums.pop(i)
            i -= 1

        return len(nums)
        '''
