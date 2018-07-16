class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        #XOR
        ans = 0
        for string in s + t:

            ans ^= ord(string)
            print(ans)

        return chr(ans)

        '''
        #str.replace
        for string in s:
            t = t.replace(string, '', 1)

        return t
        '''
