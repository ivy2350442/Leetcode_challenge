class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        def dfs(i, j):
            count = 0
            t = 0

            i_d = 1
            while i_d >= -1:
                j_d = 1
                while j_d >= -1:
                    if len(M) > i+i_d >= 0 and len(M[0]) > j+j_d >= 0:
                        count += M[i+i_d][j+j_d]
                        t += 1
                    j_d -=1
                i_d -= 1

            return int(count/t)


        ans = []
        for i in range(len(M)):
            temp = []
            for j in range(len(M[0])):
                temp.append(dfs(i, j))
            ans.append(temp)

        return ans
