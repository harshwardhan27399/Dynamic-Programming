class Solution:
    def howSum(self, targetSum : int, numbers : list[int], memo ={}) -> list[int]:
        if targetSum in memo: return memo[targetSum]
        if targetSum == 0: return []
        if targetSum < 0: return None
        for num in numbers:
            remainder = targetSum - num
            remainderResult = self.howSum(remainder, numbers, memo)
            if remainderResult is not None:
                remainderResult.append(num)
                memo[targetSum] = remainderResult
                return remainderResult
        memo[targetSum] = None
        return None

s = Solution()
print(s.howSum(8,[1,4,5]))
