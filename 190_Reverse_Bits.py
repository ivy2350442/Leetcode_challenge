class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        n_b = bin(n)[2:].zfill(32)
        n_b_r = n_b[::-1]
        ans = int(n_b_r, 2)
        return ans
