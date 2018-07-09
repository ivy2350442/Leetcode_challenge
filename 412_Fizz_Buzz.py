class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []
        for i in range(1, n+1, 1):
            temp = ''
            if i % 3 == 0:
                temp += 'Fizz'
            if i % 5 == 0:
                temp += 'Buzz'
            if i % 3 != 0 and i % 5 != 0:
                ans.append(str(i))
            else:
                ans.append(temp)

        return ans
