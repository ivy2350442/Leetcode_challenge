class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.split( )
        ans = '' #空字串中間不能有空格
        for i in range(len(s)):
            temp = s[i][::-1]
            ans = ans + temp
            if i != len(s)-1:
                ans = ans + ' '

        return ans
