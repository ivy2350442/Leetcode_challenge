class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        #set的宣告
        s = set()
        #set插入值
        s.add(n)

        while n != 1:
            temp = 0
            for i in str(n):
                temp += int(i)**2
            n = temp

            if n in s:
                return False
            else:
                s.add(n)

        return True  
