class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 2:
            return 0

        p = [1] * n

        p[0] = 0
        p[1] = 0

        for i in range(2, int(n**0.5)+1):
            if p[i] == 1:
                for j in range(2, int(n/i)+1):
                    if i*j < n:
                        p[i*j] = 0


        return p.count(1)
