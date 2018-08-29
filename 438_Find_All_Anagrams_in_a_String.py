class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        '''
        #time limit exceeded
        ans = []
        p_count = collections.Counter(p)
        for i in range(len(s) - len(p)+1):
            string = collections.Counter(s[i:i+len(p)])
            if p_count == string:
                ans.append(i)
        return ans
        '''

        ans = []
        p_count = collections.Counter(p)
        s_count = collections.Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            s_count[s[i]] += 1
            if s_count == p_count:
                ans.append(i-len(p)+1)
            s_count[s[i-len(p)+1]] -= 1
            if s_count[s[i-len(p)+1]] == 0:
                #刪除dec中 count為0 的key
                del s_count[s[i-len(p)+1]]
        return ans
