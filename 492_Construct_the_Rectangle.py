class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """


        W = int(area**0.5)

        while W:
            if area % W == 0:
                return [int(area/W), W]
            W -= 1
