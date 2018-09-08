class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ind = -2
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                temp = i - ind
                ind = i
                if temp > 2:
                    count += int((temp-2)/2)

        temp = len(flowerbed)+1 - ind
        if temp > 2:
            count += int((temp-2)/2)

        return count >= n
                
