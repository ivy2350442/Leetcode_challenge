class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        ans = 0
        while x > 0 and y > 0:
            if x % 2 != y % 2:
                ans = ans + 1
            x = int(x/2)
            y = int(y/2)


        x_count = bin(x).count('1')
        y_count = bin(y).count('1')
        ans = ans + x_count + y_count

        return ans
