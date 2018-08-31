class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = {}


    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.h.update({key:0})

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.h.pop(key, None)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.h



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
