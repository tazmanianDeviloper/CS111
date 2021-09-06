#
# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Matrix Operations  
#
# Computer Science 111   
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a rectangular 2-D list numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print('%6.2f' % matrix[r][c], end=' ')
        print()
       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

### Add your functions for options 2-5 here. ###
#option 2
def mult_row(matrix, r, m):
    """Using list comprehension all instances of matrix[r] have been multiplied
by m, stored in lc, assigned back to matrix[r]"""
    lc=[c*m for c in matrix[r]]
    matrix[r]=lc

#option 3
def add_row_into(matrix, source, dest):
    """matrxi[source] and its indices are assigned to new variables. Using a for loop,
those every instance of matrix[dest] sublist is added to the instance variable representing
matrix[source]. The accumilated value is saved ind_instance_list and ultimatly assigned to
matrix[dest]"""
    matrix_source=matrix[source]
    matrix_source_index=0
    d_instance_list=[]
    for d in matrix[dest]:
        d+=matrix_source[matrix_source_index]
        d_instance_list+=[d]
        matrix_source_index+=1
    matrix[dest]=d_instance_list
    
#option 4
def add_mult_row_into(matrix, m, source, dest):
    """Using algorithms from option 2 and 3, this function
works"""
    lc=[c*m for c in matrix[source]]
    matrix_source=lc
    matrix_source_index=0
    d_instance_list=[]
    for d in matrix[dest]:
        d+=matrix_source[matrix_source_index]
        d_instance_list+=[d]
        matrix_source_index+=1
    matrix[dest]=d_instance_list

#option 5
def transpose(matrix):
    """all variables in the sub lists of the original matrix are assigned to a new
list, then using list manipulation (slicing) the new list is sliced based on the range
of the original list as well as its sublists."""
    iv=[]
    iv_set=[]
    transposed_set=[]
    for c in range(len(matrix[0])):
        for r in range(len(matrix)):
            iv=matrix[r][c]
            iv_set+=[iv]
        transposed_set+=[iv_set]
        iv_set=[]
    return transposed_set
    
def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)

        ## add code to handle the other options here
        elif choice == 2:
            r=float(input("Enter the row:"))
            m=float(input("Enter a multiplier:"))
            mult_row(matrix, r, m)

        elif choice == 3:
            source=int(input("Enter the source index:"))
            dest=int(input("Enter the destination index:"))
            add_row_into(matrix, source, dest)

        elif choice == 4:
            m=float(input("Enter a multiplier:"))
            source=float(input("Enter the source index:"))
            dest=float(input("Enter the destination index:"))
            add_mult_row_into(matrix, m, source, dest)

        elif choice == 5:
            matrix=transpose(matrix)
                        
        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')
