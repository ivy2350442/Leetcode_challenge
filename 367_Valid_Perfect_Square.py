class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        '''
        #執行時間過長
        n = 0
        s = 0
        while n < num:
            s += 1
            n = s*s
            if s*s == num:
                return True

        return False
        '''

        n = num
        while n**2 > num:
            n = (n + num/n) // 2

        return n**2 == num
