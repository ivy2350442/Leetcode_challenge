class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """

        N_bin = bin(N)[2:]

        if N_bin.count('1') <= 1 :
            return 0
        else:
            befor = 0
            ans = 0
            for i in range(len(N_bin)):
                #注意為數字或字元
                if N_bin[i] == '1':
                    temp = i - befor 
                    befor = i
                    if temp > ans:
                        ans = temp

        return ans
