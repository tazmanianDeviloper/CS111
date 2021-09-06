#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# 2-D Lists
#
# Computer Science 111
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
# 

# IMPORTANT: This file is for your solutions to Problem 2.
# Your solutions to problem 3 should go in ps7pr3.py instead.

import random

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])
    
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')   # print nothing between values
        print() # at end of row, go to next line

#0
def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid
#1
def inner_grid(height, width):
    """When r and c are 0 or their last index 0 will be printed,
else 1 will be printed"""
    grid = create_grid(height, width)
    for r in range(height):
        for c in range(width):
            if r==0 or r==height-1:
                grid[r][c] = 0
            elif c==0 or c==width-1:
                grid[r][c] = 0
            else:
                grid[r][c]=1                
    return grid
#2
def random_grid(height, width):
    """When r and c are 0 or their coresponding last indices
0 will be printed. Else a random index between 0 and 1 will
be printed"""
    grid = create_grid(height, width)
    for r in range(height):
        for c in range(width):
            if r==0 or r==height-1:
                grid[r][c] = 0
            elif c==0 or c==width-1:
                grid[r][c] = 0
            else:
                grid[r][c]=random.choice([0,1])                
    return grid

#3
def copy(grid):
    """The input is a list of lists. In the nested loops, the first index
of the first sub list is copied to sub_set_inst. through the next itterations
this process is reapited. Once the range of a sub list is reached that sub list
is concatinated to the copied_list."""
    sub_grid_inst=[]
    sub_set_inst=[]
    copied_grid=[]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            sub_set_inst=grid[r][c]
            sub_grid_inst+=[sub_set_inst]
        copied_grid+=[sub_grid_inst]
        sub_grid_inst=[]
      
    return copied_grid

#4
def invert(grid):
    """Same algorithm a copy(grid) with added condition that
if the instance variable came to be 0, it should be switched
to 1 and vice versa"""
    sub_grid_inst=[]
    sub_set_inst=[]
    copied_grid=[]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]==0:
                #you might be abe to eliminate line 117
                grid[r][c]=1
                sub_set_inst=grid[r][c]
                sub_grid_inst+=[sub_set_inst]
            else:
                grid[r][c]=0
                sub_set_inst=grid[r][c]
                sub_grid_inst+=[sub_set_inst]                
        copied_grid+=[sub_grid_inst]
        sub_grid_inst=[]



