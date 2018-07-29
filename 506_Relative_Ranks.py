class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        nums_sort = sorted(nums, reverse=True)

        dic = {}
        for i in range(len(nums_sort)):
            if i == 0:
                dic[nums_sort[i]] = "Gold Medal"
            elif i == 1:
                dic[nums_sort[i]] = "Silver Medal"
            elif i == 2:
                dic[nums_sort[i]] = "Bronze Medal"
            else:
                dic[nums_sort[i]] = str(i + 1)

        ans = []
        for n in nums:
            ans.append(dic[n])

        return ans
