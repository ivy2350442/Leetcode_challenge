class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        ans = 0
        for point in points:
            dist = {}
            for p in points:
                d = (point[0] - p[0])**2 + (point[1] - p[1])**2
                dist[d] = 1 + dist.get(d, 0)

            for k in dist:
                ans += dist[k] * (dist[k] - 1)

        return ans
