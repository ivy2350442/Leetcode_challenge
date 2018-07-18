class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """


        if len(A) != len(B):
            return False

        #判斷式中 可以有多個相等或大小於
        elif len(A) == len(B) == 0:
            return True

        else:
            for i in range(len(A)):
                if A[i:] + A[:i] == B:
                    return True

            return False
                
