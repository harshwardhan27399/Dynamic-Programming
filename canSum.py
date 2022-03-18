from xmlrpc.client import Boolean


class Solution:
    def canSum(self, targetSum : int, numbers : list[int], memo = {} ) -> Boolean: 
        # Brut force approach
        # time n^m
        # if targetSum == 0: return True
        # if targetSum < 0: return False
        # for num in numbers:
        #     reminder = targetSum - num
        #     if self.canSum(reminder, numbers):
        #         return True
        # return False

        #optimised option
        if targetSum in memo : return memo[targetSum]
        if targetSum == 0: return True
        if targetSum < 0: return False
        
        for num in numbers:
            reminder = targetSum - num
            if self.canSum(reminder , numbers):
                memo[targetSum] = True
        memo[targetSum] = False

        return memo[targetSum]

s = Solution()
print(s.canSum(300, [7,14]))
