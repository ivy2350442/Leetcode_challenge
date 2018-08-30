class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        '''
        s_str = str.split()
        if len(pattern) != len(s_str):
            return False

        dic = {}
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if s_str[i] in dic.values():
                    return False
                dic[pattern[i]] = s_str[i]
            else:
                if dic[pattern[i]] != s_str[i]:
                    return False
        return True
        '''

        s_str = str.split()
        if len(pattern) != len(s_str):
            return False

        dic = {}
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]] != s_str[i]:
                    return False
            elif s_str[i] in dic.values():
                return False
            else:
                dic[pattern[i]] = s_str[i]
        return True
