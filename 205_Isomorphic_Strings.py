class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        '''
        #此方法的執行時間過長
        s_count = 0
        t_count = 0
        s_dic = {}
        t_dic = {}
        s_list = []
        t_list = []
        for i in range(len(s)):
            if s[i] in s_dic:
                ind = s_dic[s[i]]
                s_list[ind].append(i)

            else:
                s_dic[s[i]] = s_count
                s_count += 1
                s_list.append([i])

            if t[i] in t_dic:
                ind = t_dic[t[i]]
                t_list[ind].append(i)

            else:
                t_dic[t[i]] = t_count
                t_count += 1
                t_list.append([i])

        if s_list == t_list:
            return True
        return False
        '''

        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                if t[i] not in dic[s[i]]:
                    return False
            elif t[i] in dic.values():
                return False
            else:
                dic[s[i]] = t[i]

        return True
