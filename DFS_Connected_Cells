'''https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid'''

class Node:
    def __init__(self,i,j):
        self.id= str(i)+str(j)
        self.isVisited = False
        
def get_neigbours(i,j,grid,count):
    row_length = len(grid[0])
    col_length = len(grid)
    
    count = isValid(i-1,j-1,grid,count)  
    count = isValid(i-1,j,grid,count) 
    count = isValid(i-1,j+1,grid,count)  
    count = isValid(i,j-1,grid,count)  
    count = isValid(i,j+1,grid,count)  
    count = isValid(i+1,j-1,grid,count) 
    count = isValid(i+1,j,grid,count)  
    count = isValid(i+1,j+1,grid,count)  
    return count
    
def isValid(i,j,grid,count):
    row_length = len(grid[0])
    col_length = len(grid) 
    if i < 0 or i >= col_length or j < 0 or j >= row_length or grid[i][j] == 0:
        return count
    elif grid[i][j] == 1:
            grid[i][j] = Node(i,j) 
            count += 1
            count = get_neigbours(i,j,grid,count)
            return count
    else : 
        return count
         
 
    
def get_biggest_region(grid): 
    u_counter = 0
    max_count = 0
    for u in grid:
        v_counter = 0
        for v in u:
            count = 0
            if type(grid[u_counter][v_counter]) is int and grid[u_counter][v_counter] == 1:
                grid[u_counter][v_counter] = Node(u_counter,v_counter) 
                count += 1
                count = get_neigbours(u_counter,v_counter,grid,count)
                if count > max_count:
                    max_count = count
            v_counter += 1
        u_counter += 1
             
    return max_count

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
