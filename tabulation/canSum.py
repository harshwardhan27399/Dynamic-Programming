from xmlrpc.client import Boolean


class Solution:
    def canSum(self, targetSum : int, numbers : list[int]) -> Boolean: 
        sum_tab = [False] * (targetSum+1)

        sum_tab[0] = True
        for index in range(targetSum+1):
            if sum_tab[index] == True:
                for num in numbers:
                    if index + num <= targetSum:
                        sum_tab[index + num] = True
        # return sum_tab[targetSum]
        
        return sum_tab.count(True) -1

s = Solution()
print(s.canSum(6, [2,3,4,5]))
print(s.canSum(7, [2,3]))
print(s.canSum(300, [7,14]))
