class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        A = A.split()
        B = B.split()
        count_a = collections.Counter(A)
        count_b = collections.Counter(B)

        ans = []
        for k in count_a:
            if count_a[k] == 1 and k not in count_b:
                ans.append(k)

        for k in count_b:
            if count_b[k] == 1 and k not in count_a:
                ans.append(k)

        return ans
