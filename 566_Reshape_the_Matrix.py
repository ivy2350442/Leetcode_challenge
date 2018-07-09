class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if len(nums)*len(nums[0]) < r*c:
            return nums
        else:
            one_row = []
            #先把List合併為一row
            for i in range(len(nums)):
                one_row += nums[i]

            ans = []
            for i in range(r):
                #注意避免程式執行時間過長
                if i == 0:
                    ans.append(one_row[:c])
                else:
                    ans.append(one_row[c*i:c*(i+1)])

            return ans
