#https://leetcode.com/problems/minimum-path-sum/submissions/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid);cols=len(grid[0])
        table=[[0 for i in range(cols)] for j in range(rows)]
        
        table[0][0]=grid[0][0]
        #Fill the min values in top row
        for j in range(1,cols):
            table[0][j]=table[0][j-1]+grid[0][j]
        
        #Fill the min values in leftmost col
        for i in range(1,rows):
            table[i][0]=table[i-1][0]+grid[i][0]
        
        for i in range(1,rows):
            for j in range(1,cols):
                table[i][j]=grid[i][j]+min(table[i-1][j],table[i][j-1])

        return table[rows-1][cols-1]

def main():
    s=Solution()
    grid=[]
    
main()


