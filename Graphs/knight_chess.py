def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    # Write your code here.
    #Check if the start and end points are not 1
        row=rows;col=cols
        
        # if(grid[0][0]==1 or grid[row-1][col-1]==1):
        #     return -1
        
        visited=[ [ 0 for i in range(col) ] for j in range(row) ] 
        print(visited)
        q=[]
        ##TODO: Update dir
        dir=[[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1]]
        level=0
        
        s=[start_col,start_row]
        q.append(s)
        visited[start_row][start_col]=1

        while(not len(q)==0):
            
            size=len(q)
            
            for i in range(size):
                node=q.pop(0)
                if(node[0]==end_col and node[1]==end_row):
                    return level
                
                for j in range(len(dir)):
                    neighbor_x=dir[j][0]+node[0]
                    neighbor_y=dir[j][1]+node[1]
                    if(neighbor_x >= 0 and neighbor_y >=0 and neighbor_x<col and neighbor_y<row):
                        #print("neighbor_x:",neighbor_x,"neighbor_y:",neighbor_y)
                        if(visited[neighbor_y][neighbor_x] is 0):
                            visited[neighbor_y][neighbor_x]=1
                            q.append([neighbor_x,neighbor_y])
            level+=1
        return -1

def main():
    rows=315
    cols=315
    start_row=0
    start_col=314
    end_row=314
    end_col=0
    print(find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col))

main()
