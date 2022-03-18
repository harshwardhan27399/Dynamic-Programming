class Solution:
    def countConstruct(self, target : str, wordBank : list[str]) -> int:
        if target == '': return 1

        countWays =0
        for word in wordBank:
            if word in target:
                if target.index(word) == 0:
                    currentCount = self.countConstruct(target[len(word):], wordBank)
                    countWays += currentCount
        return countWays
    
s = Solution()
print(s.countConstruct('abcdef', ['ab' , 'cd', 'abc', 'def', 'abcd', 'ef']))
