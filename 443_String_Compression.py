class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        h = 0
        count = 1
        for i in range(1, len(chars)):

            if chars[i] == chars[i-1]:
                count += 1

            elif chars[i] != chars[i-1]:
                chars[h] = chars[i-1]
                h += 1
                if count != 1:
                    count_str = str(count)
                    for c in count_str:
                        chars[h] = c
                        h += 1
                count = 1

        chars[h] = chars[-1]
        h += 1
        if count != 1:
            count_str = str(count)
            for j in count_str:
                chars[h] = j
                h += 1

        return h   
