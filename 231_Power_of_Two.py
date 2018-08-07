class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        '''
        #執行速度過慢
        if n == 0:
            return False

        if n == 1:
            return True

        while n != 2:
            if (n % 2) != 0:
                return False
            n = n / 2

        return True
        '''

        #以二位元做and 的判斷方式較快
        if n == 0:
            return False

        if n & (n-1) == 0:
            return True
        return False
