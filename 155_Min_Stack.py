class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        #執行時間過長
        #self.s = []
        self.s = []
        #float('inf'), float('-inf') 表示正, 負無窮
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        #self.s.append(x)
        self.s.append(x)
        self.min = min(self.min, x)

    def pop(self):
        """
        :rtype: void
        """
        #self.s.pop()
        #pop 執行時間較[:-1] 長
        #self.s.pop()
        self.s = self.s[:-1]
        if len(self.s) == 0:
            self.min = float('inf')
        else:
            self.min = min(self.s)

    def top(self):
        """
        :rtype: int
        """
        #return self.s[-1]
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        #return min(self.s)
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
