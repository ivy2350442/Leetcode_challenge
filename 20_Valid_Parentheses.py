class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        '''
        #執行速度較慢
        ans = []
        for c in s:
            if c == ")":
                if len(ans) != 0 and ans[-1] == "(":
                    ans.pop()
                else:
                    return False
            elif c == "]":
                if len(ans) != 0 and ans[-1] == "[":
                    ans.pop()
                else:
                    return False
            elif c == "}":
                if len(ans) != 0 and ans[-1] == "{":
                    ans.pop()
                else:
                    return False
            else:
                ans.append(c)

        return len(ans) == 0
        '''


        stack = []
        b ={'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in b:
                stack.append(c)
            else:
                #1. 在判斷式加or中 若前一項條件已符合 則不會繼續執行後面的判斷式
                #2. 注意下式stack.pop() 此時已將stack中最後一項移除
                if len(stack) == 0 or c != b[stack.pop()]:
                    return False

        return len(stack) == 0
