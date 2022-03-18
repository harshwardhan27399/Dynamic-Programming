class Solution:
    def gridTraveller(self, rows : int, columns : int, memo = {}):
        # print('Bruitforce')
        # if rows == 0 or columns == 0: return 0
        # if rows == columns == 1: return 1
        # return self.gridTraveller(rows - 1, columns) + self.gridTraveller(rows, columns - 1)

        #print('Dynamic programming')
        new_key = str(rows)+','+str(columns)
        if str(rows)+','+str(columns) in memo: return memo[new_key]
        if rows == 0 or columns == 0: return 0
        if rows == columns == 1: return 1
        
        memo[new_key] = self.gridTraveller(rows - 1, columns, memo) + self.gridTraveller(rows, columns - 1, memo)
        return memo [new_key]


s = Solution()
print(s.gridTraveller(13,13)) 
print(s.gridTraveller(3,13)) 
print(s.gridTraveller(18,18)) 