class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a_int = int(a, 2)
        b_int = int(b, 2)
        total = a_int + b_int
        return bin(total)[2:]
