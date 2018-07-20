class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        #& 表示取交集，| 表示取聯集
        return list(set(nums1) & set(nums2))
