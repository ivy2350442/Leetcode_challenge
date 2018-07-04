class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        ans = []
        for i in range(left, right+1, 1):
            i_str = str(i)
            count = 0
            for j in range(len(i_str)):
                if i_str[j] == '0':
                    break
                elif i % int(i_str[j]) != 0:
                    break
                else:
                    count = count + 1
            if count == len(i_str):
                ans.append(i)

        return ans
