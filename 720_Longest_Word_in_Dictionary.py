class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        words.sort()

        catalog = {}
        max_l = 0
        ans_word = []
        for i in range(len(words)):
            if len(words[i]) == 1:
                catalog[words[i]] = 1

            elif words[i][:-1] in catalog:
                catalog[words[i]] = 1
                if len(words[i]) > max_l:
                    max_l = len(words[i])
                    ans_word = words[i]

        if len(ans_word) == 0:
            if len(words) != 0:
                ans_word = words[0]

        return ans_word
