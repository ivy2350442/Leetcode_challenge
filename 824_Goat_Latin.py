class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """

        vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        S = S.split( )

        ans = ''
        for i in range(len(S)):
            if S[i][0] in vowel:
                S[i] += 'ma'
            else:
                S[i] = S[i][1:] + S[i][0] + 'ma'

            S[i] += 'a' * (i+1)
            ans += S[i]
            if i != len(S) - 1:
                ans += ' '

        return ans
