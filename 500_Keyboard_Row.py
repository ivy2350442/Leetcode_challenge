class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        keyboard_0 = 'qwertyuiop'
        keyboard_1 = 'asdfghjkl'
        keyboard_2 = 'zxcvbnm'

        '''
        ans = []
        for i in range(len(words)):
            char_big = words[i]
            char = char_big.lower()
            col_0 = 0
            col_1 = 0
            col_2 = 0
            for j in range(len(keyboard_0)):
                if char.count(keyboard_0[j]) != 0:
                    col_0 += 1
                if j < len(keyboard_1):
                    if char.count(keyboard_1[j]) != 0:
                        col_1 += 1
                if j < len(keyboard_2):
                    if char.count(keyboard_2[j]) != 0:
                        col_2 += 1
                if (col_0 != 0 and col_1 != 0) or (col_1 != 0 and col_2 != 0) or (col_0 != 0 and col_2 != 0):
                    break
            if (col_0 == 0 and col_1 == 0) or (col_1 == 0 and col_2 == 0) or (col_0 == 0 and col_2 == 0):
                ans.append(char_big)
        return ans
        '''

        ans = []
        for i in words:
            #set大小寫字有差異
            if set(i.lower()).issubset(set(keyboard_0)):
                ans.append(i)
            elif set(i.lower()).issubset(set(keyboard_1)):
                ans.append(i)
            elif set(i.lower()).issubset(set(keyboard_2)):
                ans.append(i)
        return ans
