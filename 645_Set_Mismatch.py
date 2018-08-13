class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        '''
        #暴力解的方法太慢
        dic = {}
        ans = []
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for i in range(1, len(nums)+1):
            if i not in dic:
                temp = i

            elif dic[i] == 2:
                ans.append(i)

        ans.append(temp)
        return ans
        '''

        s = sum(nums)
        n = sum(set(nums))
        l = len(nums)
        t = (1 + l) *l /2

        return [s - n, t - n ]
