class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #題目輸入s 的type 並非string
        s = str(s)
        #python3 filter 的輸出為位置，利用list 包裝，再join 到str
        s = list(filter(str.isalnum, s))
        #在確定字串中皆為字母，再改變大小寫的執行速度較快
        s = ''.join(s).lower()
        return s == s[::-1]
