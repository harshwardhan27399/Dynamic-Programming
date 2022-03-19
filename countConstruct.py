class Solution:
    def countConstruct(self, target : str, wordBank : list[str], memo = {}) -> int:
        if target in memo: return memo[target] 
        if target == '': return 1

        countWays =0
        for word in wordBank:
            if word in target:
                if target.index(word) == 0:
                    currentCount = self.countConstruct(target[len(word):], wordBank, memo)
                    countWays += currentCount
        memo[target] = countWays
        return countWays
    
s = Solution()
# print(s.countConstruct('abcdef', ['ab' , 'cd', 'abc', 'def', 'abcd', 'ef']))
print(s.countConstruct('eeeeeeef', ['e' , 'ee', 'eee', 'eeee', 'eeeee', 'eeeeeef']))
