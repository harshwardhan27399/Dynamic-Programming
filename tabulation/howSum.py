class Solution:
    def howSum(self, targetSum, numbers):
        how_table = [None] * (targetSum+1)
        how_table[0] = []
        for index in range(targetSum):
            if how_table[index] is not None:
                for num in numbers:
                    if index+ num <= targetSum: 
                        how_table[index + num] = how_table[index] +[num]
        return how_table[targetSum]


s = Solution()
print(s.howSum(8,[3,4,5]))
print(s.howSum(8,[7,5]))