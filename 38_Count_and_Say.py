class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        ans = ['1']
        for num in range(n):
            count = 1
            temp = ''
            for i in range(len(ans[num])-1):
                if ans[num][i] == ans[num][i+1]:
                    count += 1
                else:
                    temp += str(count) + ans[num][i]
                    count = 1

            temp += str(count) + ans[num][-1]
            ans.append(temp)

        return ans[n-1]
