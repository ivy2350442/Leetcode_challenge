class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        R = moves.count("R")
        L = moves.count("L")
        U = moves.count("U")
        D = moves.count("D")


        if R == L and U == D:
            return True
        else:
            return False
