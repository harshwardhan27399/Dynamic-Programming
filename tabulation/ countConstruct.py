import tarfile


class Solution:
    def countConstruct(self, target, wordBank) :
        con_table = [0]*(len(target) + 1)
        con_table[0] = 1
        for index in range(len(target)+1):
            for word in wordBank:
                # if word in target[index:] and target[index:].index(word) == 0:
                if word == target[index: index +len(word)]:
                    if index + len(word) <= len(target) : 
                        con_table[index + len(word)] += con_table[index]
        return con_table[len(target)]
s = Solution()
print(s.countConstruct('abcdef', ['ab' , 'cd', 'abc', 'def', 'abcd', 'ef']))
print(s.countConstruct('eeeeeeeeeeef', ['e' , 'ee', 'eee', 'eeee', 'eeeee', 'eeeeeef']))