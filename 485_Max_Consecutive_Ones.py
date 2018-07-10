class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        ans = []

        for i in nums:
            if i == 1 :
                count += 1
            else:
                ans.append(count)
                count = 0

        #注意最後連續的1
        ans.append(count)

        return max(ans)
