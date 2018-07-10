class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        #如果n % (可取最大石頭數+1) 於0 則先手必敗
        if n % (3+1) == 0:
            return False
        else:
            return True
