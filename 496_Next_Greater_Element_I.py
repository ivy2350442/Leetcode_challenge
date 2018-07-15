class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        #特解
        #nums2 當作key 存進dictionary ,並將下一個大於自己的值存入
        dic = {}
        temp = []
        for num in nums2:
            while len(temp) and temp[-1] < num:
            #while len(temp) != 0 and temp[-1] < num
                dic[temp.pop()] = num
            temp.append(num)

        #nums1 進去dictionary 找值
        ans = []
        for num in nums1:
            ans.append(dic.get(num, -1))

        return ans


        '''
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
        '''
