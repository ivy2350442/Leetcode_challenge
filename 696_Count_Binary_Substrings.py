class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        #注意第一個直要先給
        count = [1]

        #遞迴每次判斷下一個 可省略最後加一的部分
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                count.append(1)
            else:
                count[-1] += 1

        ans = 0
        for i in range(1, len(count)):
            ans += min(count[i-1], count[i])

        return ans



        '''
        #執行速度比較慢
        if s.count('0') == len(s) or s.count('1') == len(s):
            return 0

        ans = 0
        count = 0
        con = 0
        for i in range(1, len(s), 1):

            if s[i-1] != s[i]:
                count += 1
                if count == 2:
                    ans += min(s[con:i].count('1'), s[con:i].count('0'))
                    con = temp
                    count = 1
                temp = i

            if i == len(s)-1:
                ans += min(s[con:].count(s[i]), s[con:].count(s[con]))

        return ans
        '''
