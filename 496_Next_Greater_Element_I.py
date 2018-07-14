class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = []
        for i in range(len(nums1)):
            next_index = nums2.index(nums1[i]) + 1
            if next_index < len(nums2):
                while (next_index < len(nums2)):
                    if nums2[next_index] > nums1[i]:
                        ans.append(nums2[next_index])
                        break
                    else:
                        next_index += 1
                if len(ans) != i + 1:
                    ans.append(-1)
            else:
                ans.append(-1)

        return ans
