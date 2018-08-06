class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #counter 的key 不會由小排序到大
        count = collections.Counter(nums)

        ans = 0
        for key in count:
            if key+1 in count:
                ans = max(ans, count[key] + count[key+1])

        return ans
