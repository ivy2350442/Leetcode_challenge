class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ans = 0
        count = collections.Counter(nums)
        for c in count:
            if k>0 and c+k in count or k==0 and count[c]>1:
                ans += 1

        return ans
