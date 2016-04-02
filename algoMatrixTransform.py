

def vertical_downward(m,n,row,col,R,matrix=None,new_matrix=None):
    """Gets row elements of the left side of the
        box """
    edge_row = row
    edge_col = col
    while row < (edge_row + m ) or row == (edge_row + m):
         
        matrix_value = matrix[row][col] 
        if R == 0:
            new_matrix [row][col] = matrix_value
        else:
            xy_pos = compute_new_pos(m,n,row,col, R,edge_row,edge_col,"left")
            new_matrix [xy_pos[0]][xy_pos[1]] = matrix_value
        row += 1
    return new_matrix

def compute_new_pos(m,n,row,col,R,edge_row,edge_col,location):
    """computes new position for a particular element at row,col by
        shifting the m x n matrix with row_col by R
        location can be either "top","bottom","left","right"
        m x n is the dimension of the box in focus"""
    new_col = 0
    new_row = 0
    col1= col
    row1 = row
    while R > 0:
        if location  == "top":
            #new_col = R - col
            if R > col - edge_col:
                R = R - (col - edge_col)
                col = edge_col
                row = row
                location = "left" #move left <=
            else:
                new_col = col - R
                new_row = row
                R = 0
             
        elif location == "left":
            if R > (edge_row + m) - row:
                R = R - ((edge_row + m) - row)
                row = edge_row + m
                col = col
                location = "bottom" #move down
            else:
                new_row = R + row
                new_col = col
                R = 0
             
        elif location == "bottom":
            if R > (edge_col + n) - col:
                R = R - ((edge_col + n) - col)
                col = (edge_col + n)
                row = row
                location = "right" #move right =>
            else:
                new_col = R + col
                new_row = row
                R = 0
             
        elif location == "right":
            if R > row - edge_row:
                R = R - (row - edge_row)
                row = edge_row
                col = col
                location = "top" #move up 
            else:
                new_row = row - R
                new_col = col
                R = 0
##    print row,col,new_row,new_col,edge_row,edge_col,location,m,n
    return [new_row,new_col]
        

def horizontal_forward(m,n,row,col,R,matrix=None,new_matrix=None):
    """Gets column elements of the bottom side of the
        box """
    edge_row = row
    edge_col = col   
    while col < (edge_col + n) or col == (edge_col + n):
        matrix_value = matrix[edge_row + m][col]
        if R == 0:
            new_matrix [edge_row + m][col] = matrix_value
        else:
            xy_pos = compute_new_pos(m,n,(edge_row + m),col,R,edge_row,edge_col,"bottom")
            new_matrix[xy_pos[0]][xy_pos[1]] = matrix_value
        col += 1     
    return new_matrix
    
def vertical_upward(m,n,row,col,R,matrix=None,new_matrix=None):
    """Gets row elements of the right side of the
        box """
    edge_row = row
    edge_col = col  
    while row < (edge_row + m) or row == (edge_row + m):
        matrix_value = matrix[row][col + n]
        if R == 0:
            new_matrix [row][col+ n] = matrix_value
        else:
            xy_pos = compute_new_pos(m,n,row,(col + n), R,edge_row,edge_col,"right")
            new_matrix [xy_pos[0]][xy_pos[1]] = matrix_value
        row += 1    
    return new_matrix

def horizontal_backward(m,n,row,col,R,matrix=None,new_matrix=None):
    """Gets column elements of the top side of the
        box """
    edge_row = row
    edge_col = col
    while col < (edge_col + n) or col == (edge_col + n):
        matrix_value = matrix[row][col]
        if R == 0:
            new_matrix [row][col] = matrix_value
        else:
            xy_pos = compute_new_pos(m,n,row,col,R,edge_row,edge_col,"top")
            new_matrix[xy_pos[0]][xy_pos[1]] = matrix_value
        col += 1
        
    return new_matrix


def run():
    from random import randint
    M = 4
    N = 2
    S = 40
    
    matrix = [[randint(1,14) for col in xrange(N)] for row in xrange(M)]
##    matrix = [[11, 2, 7, 12],[13, 1, 7, 12],[1, 2, 4, 2],[1, 9, 2, 8],[8, 8, 13, 9]]
    #Create a matrix with same size as input matrix M x N for rotation
    new_matrix = [[0 for col in xrange(N)] for row in xrange(M)]
    for i in matrix:
        print i
    numerator = N if M > N else M
    for i in xrange(numerator/2):
        print matrix[i][i]
        row = i
        col = i
        mm =  M - (2 * i)
        nn = N - (2 * i)
        R = S % ((2 *mm )+ ((nn - 2)* 2))        
        m = mm -1
        n = nn -1
        
        new_matrix = vertical_downward(m,n,row,col,R,matrix,new_matrix)        
        new_matrix = horizontal_forward(m,n,row,col,R,matrix,new_matrix)
        new_matrix = vertical_upward(m,n,row,col,R,matrix,new_matrix)
        new_matrix = horizontal_backward(m,n,row,col,R,matrix,new_matrix)

    print "************"
    for i in new_matrix:
        print i
    

run()


        
