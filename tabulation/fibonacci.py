class Solution:
    def getFibonacci(self, n):
        fib_tab = [0] * (n+1)
        fib_tab[1] = 1
        for index in range(1,n+1):
            if index+1 <= n :fib_tab[index +1] += fib_tab[index]

            if index+2 <= n :fib_tab[index +2] += fib_tab[index]
        return fib_tab[index]

s = Solution()
print(s.getFibonacci(50))