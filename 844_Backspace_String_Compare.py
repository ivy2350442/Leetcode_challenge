class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = []
        t = []

        for i in range(len(S)):
            if S[i] == '#':
                #注意:(1) pop 在空次串無法使用 (2) 用list[:-1] 的速度比pop 快
                s = s[:-1]
            else:
                s.append(S[i])

        for i in range(len(T)):
            if T[i] == '#':
                t = t[:-1]
            else:
                t.append(T[i])

        if s == t:
            return True
        else:
            return False
