class Solution:
    def allConstructs(self, target : str, wordBank : list[str], memo = {}) -> list[list[str]]:
        if target in memo: return memo[target]
        if target == '': return [[]]
        result = []
        for word in wordBank:
            if word in target:
                if target.index(word) == 0:
                    suffixWays = self.allConstructs(target[len(word):], wordBank, memo)
                    targetWays = []
                    for way in suffixWays: targetWays.append([word] +way)
                    for way in targetWays: result.append(way)
        memo[target] = result
        return result
    # Brut force
    # def allConstructs(self, target : str, wordBank : list[str]) -> list[list[str]]:
    #     if target == '': return [[]]
    #     result = []
    #     for word in wordBank:
    #         if word in target:
    #             if target.index(word) == 0:
    #                 suffixWays = self.allConstructs(target[len(word):], wordBank)
    #                 targetWays = []
    #                 for way in suffixWays: targetWays.append([word] +way)
    #                 for way in targetWays: result.append(way)
    #     return result


s = Solution()
print(s.allConstructs('abcdef', ['ab' , 'cd', 'abc', 'def', 'abcd', 'ef']))
print(s.allConstructs('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
                ['e' , 'ee', 'eee', 'eeee', 'eeeee', 'eeeeeef']))
