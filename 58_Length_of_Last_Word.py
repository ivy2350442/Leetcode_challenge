class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #strip(' ') 刪除頭尾出現的空格
        s = s.strip(' ')
        #注意s.split(' ') 與s.split() 不同
        s = s.split(' ')
        return len(s[-1])
        
