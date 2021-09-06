#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Conway's Game of Life
#
# Computer Science 111  
#

# IMPORTANT: this file is for your solutions to Problem 3.
# Your solutions to Problem 2 should go in ps7pr2.py instead.

from ps7pr2 import *
from gol_graphics import *
import random

#1
def count_neighbors(cellr, cellc, grid):
    """Using if/then conditions the count is incriminated by one every time the neighboring
cell is 1"""
    count=0
    cell=grid[cellr][cellc]
    if cellr==0 or cellr==len(grid) or cellc==0 or cellc==len(grid[0]):
        print("The input inetegers must be bigger than zero but less than max-values")
    else:
        if cell==0:
            if cell+grid[cellr][cellc+1]==1:
                count+=1
            if cell+grid[cellr][cellc-1]==1:
                count+=1
                
            if cell+grid[cellr-1][cellc-1]==1:
                count+=1
            if cell+grid[cellr-1][cellc]==1:
                count+=1
            if cell+grid[cellr-1][cellc+1]==1:
                count+=1

            if cell+grid[cellr+1][cellc-1]==1:
                count+=1
            if cell+grid[cellr+1][cellc]==1:
                count+=1
            if cell+grid[cellr+1][cellc+1]==1:
                count+=1
        else:
            if cell+grid[cellr][cellc+1]==2:
                count+=1
            if cell+grid[cellr][cellc-1]==2:
                count+=1
                
            if cell+grid[cellr-1][cellc-1]==2:
                count+=1
            if cell+grid[cellr-1][cellc]==2:
                count+=1
            if cell+grid[cellr-1][cellc+1]==2:
                count+=1

            if cell+grid[cellr+1][cellc-1]==2:
                count+=1
            if cell+grid[cellr+1][cellc]==2:
                count+=1
            if cell+grid[cellr+1][cellc+1]==2:
                count+=1
            
    return count

#2
def next_gen(grid):
    """Using algorithms from ps7pr2, first I assigned 0 to the first row and the last row.
0 has been assigned to the first index and the last index of each row as well. All inner cells are sent
to count_neighbors() to figure out how many live neighbors they have. Based on thier live neighbors,
that cell is either killed, revived, or kept untouched."""
    sub_grid_inst=[]
    sub_set_inst=[]
    new_grid=[]
    for cellr in range(len(grid)):
        for cellc in range(len(grid[0])):
            if cellr==0 or cellr==len(grid)-1:
                sub_set_inst= 0
                sub_grid_inst+=[sub_set_inst]
            elif cellc==0 or cellc==len(grid[0])-1:
                sub_set_inst= 0
                sub_grid_inst+=[sub_set_inst]
            else:
                cell_count=count_neighbors(cellr, cellc, grid)
                if cell_count<2:
                    sub_set_inst=0
                    sub_grid_inst+=[sub_set_inst]
                elif cell_count>3:
                    sub_set_inst=0
                    sub_grid_inst+=[sub_set_inst]
                elif cell_count==3:
                    sub_set_inst=1
                    sub_grid_inst+=[sub_set_inst]
                else:
                    sub_set_inst=grid[cellr][cellc]
                    sub_grid_inst+=[sub_set_inst]
        new_grid+=[sub_grid_inst]
        sub_grid_inst=[]
      
    return new_grid
    
    
                
            
            
            
    
    
    

    
            
                

    
