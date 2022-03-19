class Solution:
    def gridTraveller(harsh, m, n):
        grid = [[0]* (n+1) for i in range(m+1)] 
        grid[1][1] = 1
        # print(grid)
        for i in range(m+1):
            for j in range(n+1):
                if i+1 <= m: grid[i+1][j] += grid[i][j]
                if j+1 <= n: grid[i][j+1] += grid[i][j]
        return grid[m][n]
s = Solution()
print(s.gridTraveller(3,2))
print(s.gridTraveller(13,13))
print(s.gridTraveller(3,13))
print(s.gridTraveller(18,18))