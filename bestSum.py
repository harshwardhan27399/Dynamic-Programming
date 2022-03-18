class Solution:
    def bestSum(self, targetSum : int, numbers : list[int], memo = {}):
        # Brute Force
        if targetSum in memo: return memo[targetSum]
        if targetSum == 0: return []
        if targetSum < 0: return None
        shortestCombination = []
        for num in numbers:
            remainder = targetSum - num
            remainderResult = self.bestSum(remainder, numbers, memo)
            
            if remainderResult is not None:
                combination = remainderResult + [num]
                if len(shortestCombination) == 0 or len(shortestCombination) > len(combination):
                    shortestCombination = combination
                   
        if len(shortestCombination) > 0:
            memo[targetSum] = shortestCombination
            return shortestCombination
        else: 
            memo[targetSum] = []
            return None
        
        
        # # Brute Force
        # if targetSum == 0: return []
        # if targetSum < 0: return None
        # shortestCombination = []
        # for num in numbers:
        #     remainder = targetSum - num
        #     remainderResult = self.bestSum(remainder, numbers)
            
        #     if remainderResult is not None:
        #         combination = remainderResult + [num]
        #         if len(shortestCombination) == 0 or len(shortestCombination) > len(combination):
        #             shortestCombination = combination
        #             print(shortestCombination)
                    
                    
        # if len(shortestCombination) > 0:return shortestCombination
        # else: return None


s = Solution()
print(s.bestSum(7,[1,2,4,3,5]))
print(s.bestSum(100,[1,2,5,25]))