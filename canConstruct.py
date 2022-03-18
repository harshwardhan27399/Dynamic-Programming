from xmlrpc.client import Boolean


class Solution:
    # Optimized
    def canConstruct(self, target : str, wordBank : list[str], memo = {} ) -> Boolean:
        if target in memo: return True
        if target == '': return True
        for word in wordBank:
            if word in target:
                if target.index(word) == 0:
                    if self.canConstruct(target[len(word):] , wordBank, memo):
                        memo[target] = True
                        return True
        memo[target] = False
        return False

    # Bruteforce
    # def canConstruct(self, target : str, wordBank : list[str] ) -> Boolean:
    #     if target == '': return True

    #     for word in wordBank:
    #         if word in target:
    #             if target.index(word) == 0:
    #                 if self.canConstruct(target[len(word):] , wordBank):
    #                     return True
    #     return False
    
s = Solution()
print(s.canConstruct('abdef', ['ab' , 'cd', 'abc', 'def', 'abcd']))