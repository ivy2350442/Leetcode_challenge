class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        n_bin = bin(n)[2:]
        for i in range(len(n_bin)):
            if i != 0 and n_bin[i] == n_bin[i-1]:
                return False
        return True
