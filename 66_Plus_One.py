class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        length = len(digits) - 1
        while (length != -1):
            if digits[length] != 9:
                digits[length] += 1
                break
            else:
                digits[length] = 0
                length -= 1

        if length == -1:
            digits.insert(0, 1)

        return digits

        
