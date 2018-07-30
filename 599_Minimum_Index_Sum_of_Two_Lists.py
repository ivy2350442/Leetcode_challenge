class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        list2_dic = {}
        for ind, res in enumerate(list2):
            list2_dic[res] = ind

        sum = 2000
        ans = []
        for i in range(len(list1)):
            #list 及dict 尋找值的時間複雜度不同
            if list1[i] in list2_dic:
            #if list1[i] in list2:
                temp = i + list2_dic[list1[i]]
                if temp < sum:
                    sum = temp
                    ans = []
                    ans.append(list1[i])
                elif temp == sum:
                    ans.append(list1[i])

        return ans
