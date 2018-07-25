class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        r_set = set(ransomNote)
        print(r_set)

        for s in r_set:
            if ransomNote.count(s) > magazine.count(s):

                return False

        return True
