class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        paragraph = paragraph.replace("!", '')
        paragraph = paragraph.replace("?", '')
        paragraph = paragraph.replace("'", '')
        paragraph = paragraph.replace(",", '')
        paragraph = paragraph.replace(";", '')
        paragraph = paragraph.replace(".", '')
        paragraph = paragraph.lower()
        paragraph = paragraph.split(' ')

        #collections.Counter
        count = collections.Counter(paragraph)
        # Counter({'hit': 3, 'ball': 2, 'a': 1, 'far': 1, 'was': 1, 'after': 1, 'flew': 1, 'the': 1, 'it': 1, 'bob': 1})

        ans, m = '', 0
        ban_set = set(banned)

        #counter for 及if 的方式類似dictionary
        for word in count:
            if count[word] > m and word not in ban_set:
                ans, m = word, count[word]

        return ans
