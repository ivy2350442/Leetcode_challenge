class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        encode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        ans_str = []
        for i in range(len(words)):
            temp = " "
            for j in range(len(words[i])):
                ascll = ord(words[i][j]) - 97
                temp = temp + encode[ascll]
            ans_str.append(temp)


        answer = []
        for i in range(len(ans_str)):
            if len(answer) == 0:
                answer.append(ans_str[i])
            else:
                if answer.count(ans_str[i]) == 0:
                    answer.append(ans_str[i])

        ans = len(answer)

        return ans
