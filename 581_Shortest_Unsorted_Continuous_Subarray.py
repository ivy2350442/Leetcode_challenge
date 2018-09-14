class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_s = sorted(nums)
        l, r = 0, len(nums)-1
        l_p , r_p = 0, 0
        while l_p == 0 or r_p == 0:
            if l_p == 0:
                if nums[l] != nums_s[l]:
                    l_p = 1
                else:
                    l += 1

            if r_p == 0:
                if nums[r] != nums_s[r]:
                    r_p = 1
                else:
                    r -= 1

            if l >= r:
                return 0

        return r-l+1
            
