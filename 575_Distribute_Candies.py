class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        kind = set(candies)
        ans = 0
        if len(kind) > int(len(candies)/2) :
            ans = int(len(candies)/2)
        else:
            ans = len(kind)

        return ans
