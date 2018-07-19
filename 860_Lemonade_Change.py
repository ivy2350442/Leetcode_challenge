class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        dic = {5:0, 10:0, 20:0}

        for i in bills:

            if i == 10:
                if dic[5] < 1:
                    return False
                dic[5] -= 1

            elif i == 20:
                #temp 的使用
                temp = 0
                if dic[5] == 0 or dic[10] == 0:
                    temp = 1
                else:
                    dic[5] -= 1
                    dic[10] -= 1

                if temp == 1:
                    if dic[5] < 3:
                        return False
                    else:
                        dic[5] -= 3

            dic[i] += 1

        return True
