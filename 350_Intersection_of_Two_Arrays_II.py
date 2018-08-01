class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        inter = list(set(nums1) & set(nums2))
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)

        inter_min = 0
        ans = []
        for i in inter:
            inter_min = min(count1[i], count2[i])
            for j in range(inter_min):
                ans.append(i)

        return ans
