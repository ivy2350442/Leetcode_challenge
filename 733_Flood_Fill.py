class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        fix = image[sr][sc]
        if fix == newColor:
            return image

        def dfs(sr, sc):
            if image[sr][sc] == fix:
                image[sr][sc] = newColor

                if len(image)-1 > sr:
                    dfs(sr+1, sc)
                if sr > 0:
                    dfs(sr-1, sc)
                if len(image[0])-1 > sc:
                    dfs(sr, sc+1)
                if sc > 0:
                    dfs(sr, sc-1)

        dfs(sr, sc)

        return image
    
