class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain = {}
        for i in range(len(cpdomains)):
            sets = cpdomains[i].split( )
            sets[0] = int(sets[0])

            while (sets[1].count('.') > 0):
                if sets[1] in domain.keys():
                    domain[sets[1]] += sets[0]
                else:
                    domain.update({sets[1]: sets[0]})
                temp = sets[1].split('.', 1)
                sets[1] = temp[1]

                if sets[1].count('.') == 0:
                    if sets[1] in domain.keys():
                        domain[sets[1]] += sets[0]
                    else:
                        domain.update({sets[1]: sets[0]})

        ans = []
        for key in domain.keys():  #dictionary 的 for 要注意!
            ans.append(str(domain[key]) + " " + key)

        return ans
