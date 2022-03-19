class Solution:
    def bestSum(self, targetSum, numbers):
        best_table = [None] * (targetSum+1)
        best_table[0] = []
        for index in range(targetSum):
            if best_table[index] is not None:
                for num in numbers:
                    if index+ num <= targetSum: 
                        if best_table[index + num] is None or len(best_table[index + num]) > len(best_table[index] +[num]):
                            best_table[index + num] = best_table[index] +[num]
                        
        return best_table[targetSum]


s = Solution()
print(s.bestSum(8,[1,2,3,4,8]))
print(s.bestSum(8,[7,5,1, 2]))