class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.s.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        n = self.s.pop()
        return n


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        n = self.s[-1]
        return n


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.s) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
