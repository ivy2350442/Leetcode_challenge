class Solution:


    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """

        '''
        def prime(num):
            if num == 1:
                return 0
            else:
                for i in range(1, num, 1):
                    if i != 1 and num % i == 0:
                        return 0
                return 1

        ans = 0
        for i in range(R-L+1):
            ans += prime(bin(L+i)[2:].count('1'))

        return ans
        '''

        #10000的二進位 最多約只有20位 自己宣告即可
        prime = [2,3,5,7,11,13,17,19,23,29]

        ans = 0
        for i in range(R-L+1):
            #原本就沒有重複元素 不需要再轉成set 增加runtime
            if bin(L+i)[2:].count('1') in prime:
                ans += 1

        return ans
