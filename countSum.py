class Solution:
    def countSum(self, targetSum : int, numbers : list[int], memo = {}) -> int:
        if targetSum in memo: return memo[targetSum]
        if targetSum == 0: return 1
        if targetSum < 0: return 0

        countWays = 0

        for num in numbers:
            reminder = targetSum - num
            countWays += self.countSum(reminder, numbers, memo)
            memo[targetSum] = countWays

        return countWays

s = Solution()
print(s.countSum(7,[1,3,4,7]))