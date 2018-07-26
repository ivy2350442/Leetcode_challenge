class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        '''
        #two point
        f = 0
        l = len(numbers) - 1

        while (numbers[f] + numbers[l] != target):
            if numbers[f] + numbers[l] > target:
                l -= 1
            else:
                f += 1

        return [f+1, l+1]
        '''

        '''
        #enumerate
        dic = {}
        for i, n in enumerate(numbers, start=1):
            if target - n in dic:
                return [dic[target - n], i]
            dic[n] = i
        '''

        dic = {}
        for n in range(len(numbers)):
            if target - numbers[n] in dic:
                return [dic[target - numbers[n]]+1, n+1]
            dic[numbers[n]] = n
        
