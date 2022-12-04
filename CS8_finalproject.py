# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:51:34 2021

@author: MateBook
"""
# Olivia Dong, CS 8 (S21)
import copy


def read_configuration(filename):
    """ 
    take a filename as input and return a list,
        where every line from the file is its own list,
        which contains each whitespace-separated value
        as its element.
    """
    grid = [] # create a new list
    file = open(filename) # open file
    rows = file.readlines() # read content in file in a list
    for row in rows:
        grid.append(row.split())
    grid = [[int(num) for num in row] for row in grid]
    file.close() # close file
 
    return grid


def vampirize(city_grid, position):
    '''
    
    The vampire function takes in the grid and a position as a tuple. 
    For the provided position, it updates all adjacent cells 
    (up/down/left/right) in the grid to be 1 (an integer). 
     The vampirize function return a new grid after adjacent 0's turned to 1's.

    Returns
    If the grid is empty, return -1.
    If the grid contains a single list with just 1 element in it, return -1.
    If the position coordinates are outside of the grid, return None.
    
    '''
    # extract the row and column number
    posit_row = position[0]
    posit_column = position[1]
    grid = copy.deepcopy(city_grid)
    # check if grid is empty
    if len(grid) == 0:
        return -1
    # check if there is only one list
    elif len(grid) == 1:
        if len(grid[0]) == 1:
            return -1
        elif position[0] > (len(grid) - 1) or position[1] > (len(grid[0]) - 1):
            return None
        else:
            # when there is one long row
            if posit_row == 0 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                return grid
            if posit_row == 0 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                return grid
            else:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                
                return grid
            


    if len(grid) == 2:
        
        if position[0] > (len(grid) - 1) or position[1] > (len(grid[0]) - 1):
            return None
        # 2*1 grid
        elif len(grid[0]) == 1:
            if posit_row == 0 and posit_column == 0:
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                return grid
            if posit_row == 1:
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
        # 2*2 grid
        elif len(grid[0]) == 2:
            if posit_row == 0 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                return grid # return the grid after vampirization
            if posit_row == 0 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                return grid
            if posit_row == len(grid) - 1 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
            if posit_row == len(grid) - 1 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
            
        # 2*n grid
        elif len(grid[0]) > 2:

            if posit_row == 0 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                return grid # return the grid after vampirization
            if posit_row == 0 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                return grid
            if posit_row == len(grid) - 1 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
            if posit_row == len(grid) - 1 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
            # when the vampire is on the edge.
            if posit_row == 0:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                return grid
            if posit_row == len(grid) - 1:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
            elif posit_column == 0:
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                return grid
            elif posit_column == len(grid[0])-1:
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                return grid
        
        
    elif len(grid) > 2:
        if position[0] > (len(grid) - 1) or position[1] > (len(grid[0]) - 1):
            return None 
        # columns with only one element
        if len(grid[0]) == 1:
            if posit_row == 0 and posit_column == 0:
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                return grid # return the grid after vampirization
            if posit_row == len(grid) - 1 and posit_column == 0:
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
            else:
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
        # n*2 grid
        if len(grid[0]) == 2:
            if posit_row == 0 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                if grid[posit_row+1][posit_column] == 0:
                     grid[posit_row+1][posit_column] = 1
                return grid # return the grid after vampirization
            if posit_row == 0 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                return grid
            if posit_row == len(grid) - 1 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
            if posit_row == len(grid) - 1 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
            if posit_column == 0:
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                return grid
            if posit_column == len(grid[0])-1:
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                return grid
        # size bigger than 3*3
        if len(grid[0]) > 2:
        # when the vampire is at the corners.
            if posit_row == 0 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                return grid # return the grid after vampirization
            if posit_row == 0 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                return grid
            if posit_row == len(grid) - 1 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
            if posit_row == len(grid) - 1 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
            # when the vampire is on the edge.
            if posit_row == 0:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                return grid
            if posit_row == len(grid) - 1:
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                return grid
            elif posit_column == 0:
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                return grid
            elif posit_column == len(grid[0])-1:
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                return grid
            # when the vampire is in the middle if grid
            else:
                if grid[posit_row-1][posit_column] == 0:
                    grid[posit_row-1][posit_column] = 1
                if grid[posit_row+1][posit_column] == 0:
                    grid[posit_row+1][posit_column] = 1
                if grid[posit_row][posit_column-1] == 0:
                    grid[posit_row][posit_column-1] = 1
                if grid[posit_row][posit_column+1] == 0:
                    grid[posit_row][posit_column+1] = 1
                return grid
        
def cure(city_grid, position):
    '''
    
    The vampire function takes in the grid and a position as a tuple. 
    For the provided position, it updates all adjacent cells 
    (up/down/left/right) in the grid to be 1 (an integer). 
     The vampirize function return a new grid after adjacent 0's turned to 1's.

    Returns
    If the grid is empty, return -1.
    If the grid contains a single list with just 1 element in it, return -1.
    If the position coordinates are outside of the grid, return None.
    
    '''
    # extract the row and column number
    posit_row = position[0]
    posit_column = position[1]
    grid = copy.deepcopy(city_grid)
    
    if len(grid) == 0:
        return -1
    elif len(grid) == 1:
        if len(grid[0]) == 1:
            return -1
        elif position[0] > (len(grid) - 1) or position[1] > (len(grid[0]) - 1):
            return None
        else:
            if posit_row == 0 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                return grid
            if posit_row == 0 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                return grid
            else:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                
                return grid
            

    # two rows
    if len(grid) == 2:
        
        if position[0] > (len(grid) - 1) or position[1] > (len(grid[0]) - 1):
            return None
        # 2*1 grid
        elif len(grid[0]) == 1:
            if posit_row == 0 and posit_column == 0:
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                return grid
            if posit_row == 1:
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                return grid
        # 2*2 grid
        elif len(grid[0]) == 2:
            if posit_row == 0 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row+1][posit_column+1] == 1:
                    grid[posit_row+1][posit_column+1] = 0
                return grid # return the grid after vampirization
            if posit_row == 0 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row+1][posit_column-1] == 1:
                    grid[posit_row+1][posit_column-1] = 0
                return grid
            if posit_row == len(grid) - 1 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row-1][posit_column+1] == 1:
                    grid[posit_row-1][posit_column+1] = 0
                return grid
            if posit_row == len(grid) - 1 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row-1][posit_column-1] == 1:
                    grid[posit_row-1][posit_column-1] = 0
                return grid
            
        # 2*n grid
        elif len(grid[0]) > 2:

            if posit_row == 0 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row+1][posit_column+1] == 1:
                    grid[posit_row+1][posit_column+1] = 0
                return grid # return the grid after vampirization
            if posit_row == 0 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row+1][posit_column-1] == 1:
                    grid[posit_row+1][posit_column-1] = 0
                return grid
            if posit_row == len(grid) - 1 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row-1][posit_column+1] == 1:
                    grid[posit_row-1][posit_column+1] = 0
                return grid
            if posit_row == len(grid) - 1 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row-1][posit_column-1] == 1:
                    grid[posit_row-1][posit_column-1] = 0
                return grid
            # when the vampire is on the edge.
            if posit_row == 0:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row+1][posit_column+1] == 1:
                    grid[posit_row+1][posit_column+1] = 0
                if grid[posit_row+1][posit_column-1] == 1:
                    grid[posit_row+1][posit_column-1] = 0
                return grid
            if posit_row == len(grid) - 1:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row-1][posit_column+1] == 1:
                    grid[posit_row-1][posit_column+1] = 0
                if grid[posit_row-1][posit_column-1] == 1:
                    grid[posit_row-1][posit_column-1] = 0
                return grid
            elif posit_column == 0:
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row+1][posit_column+1] == 1:
                    grid[posit_row+1][posit_column+1] = 0
                if grid[posit_row-1][posit_column+1] == 1:
                    grid[posit_row-1][posit_column+1] = 0
                return grid
            elif posit_column == len(grid[0])-1:
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row+1][posit_column-1] == 1:
                    grid[posit_row+1][posit_column-1] = 0
                if grid[posit_row-1][posit_column-1] == 1:
                    grid[posit_row-1][posit_column-1] = 0
                return grid
        
    # when the row is bigger than 2  
    elif len(grid) > 2:
        if position[0] > (len(grid) - 1) or position[1] > (len(grid[0]) - 1):
            return None 
        # a long column
        if len(grid[0]) == 1:
            if posit_row == 0 and posit_column == 0:
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                return grid # return the grid after vampirization
            if posit_row == len(grid) - 1 and posit_column == 0:
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                return grid
            else:
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                return grid
        # n*2 grid
        if len(grid[0]) == 2:
            if posit_row == 0 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row+1][posit_column] == 1:
                     grid[posit_row+1][posit_column] = 0
                if grid[posit_row+1][posit_column+1] == 1:
                    grid[posit_row+1][posit_column+1] = 0
                return grid # return the grid after vampirization
            if posit_row == 0 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row+1][posit_column-1] == 1:
                    grid[posit_row+1][posit_column-1] = 0
                return grid
            if posit_row == len(grid) - 1 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row-1][posit_column+1] == 1:
                    grid[posit_row-1][posit_column+1] = 0
                return grid
            if posit_row == len(grid) - 1 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row-1][posit_column-1] == 1:
                    grid[posit_row-1][posit_column-1] = 0
                return grid
            if posit_column == 0:
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row+1][posit_column+1] == 1:
                    grid[posit_row+1][posit_column+1] = 0
                if grid[posit_row-1][posit_column+1] == 1:
                    grid[posit_row-1][posit_column+1] = 0
                return grid
            if posit_column == len(grid[0])-1:
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row+1][posit_column-1] == 1:
                    grid[posit_row+1][posit_column-1] = 0
                if grid[posit_row-1][posit_column-1] == 1:
                    grid[posit_row-1][posit_column-1] = 0
                return grid
            
        # n*n grid
        if len(grid[0]) > 2:
            if position[0] > (len(grid) - 1) or position[1] > (len(grid[0]) - 1):
                return None        
        # when the vampire is at the corners.
            if posit_row == 0 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row+1][posit_column+1] == 1:
                    grid[posit_row+1][posit_column+1] = 0
                return grid
            if posit_row == 0 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row+1][posit_column-1] == 1:
                    grid[posit_row+1][posit_column-1] = 0
                return grid
            if  posit_row == len(grid) - 1 and posit_column == 0:
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row-1][posit_column+1] == 1:
                    grid[posit_row-1][posit_column+1] = 0
                return grid
            if  posit_row == len(grid) - 1 and posit_column == len(grid[0])-1:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row-1][posit_column-1] == 1:
                    grid[posit_row-1][posit_column-1] = 0
                return grid
            # when the position is on the edge
            if posit_row == 0:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row+1][posit_column+1] == 1:
                    grid[posit_row+1][posit_column+1] = 0
                if grid[posit_row+1][posit_column-1] == 1:
                    grid[posit_row+1][posit_column-1] = 0
                return grid
            if posit_row == len(grid) - 1:
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row-1][posit_column+1] == 1:
                    grid[posit_row-1][posit_column+1] = 0
                if grid[posit_row-1][posit_column-1] == 1:
                    grid[posit_row-1][posit_column-1] = 0
                return grid
            elif posit_column == 0:
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row+1][posit_column+1] == 1:
                    grid[posit_row+1][posit_column+1] = 0
                if grid[posit_row-1][posit_column+1] == 1:
                    grid[posit_row-1][posit_column+1] = 0
                return grid
            elif posit_column == len(grid[0])-1:
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row+1][posit_column-1] == 1:
                    grid[posit_row+1][posit_column-1] = 0
                if grid[posit_row-1][posit_column-1] == 1:
                    grid[posit_row-1][posit_column-1] = 0
                return grid
            # when the position is in the middle
            else:
                if grid[posit_row-1][posit_column] == 1:
                    grid[posit_row-1][posit_column] = 0
                if grid[posit_row+1][posit_column] == 1:
                    grid[posit_row+1][posit_column] = 0
                if grid[posit_row][posit_column-1] == 1:
                    grid[posit_row][posit_column-1] = 0
                if grid[posit_row][posit_column+1] == 1:
                    grid[posit_row][posit_column+1] = 0
                if grid[posit_row+1][posit_column-1] == 1:
                    grid[posit_row+1][posit_column-1] = 0
                if grid[posit_row+1][posit_column+1] == 1:
                    grid[posit_row+1][posit_column+1] = 0
                if grid[posit_row-1][posit_column-1] == 1:
                    grid[posit_row-1][posit_column-1] = 0
                if grid[posit_row-1][posit_column+1] == 1:
                    grid[posit_row-1][posit_column+1] = 0
                return grid      




def next_day(origin_grid):
    '''
    Given a grid as a parameter, returns the updated grid of next day. 
    Return unchanged grid if it is empty or contains only one element which
    also contains only one element.
    Otherwise, some human in the original grid are vampirized. 
    Call vampirize in this function. 
    Get a list which contains positions of vampire. 
    Itenerating over the list to vampirize humans adjacent to vampire.

    '''
    if len(origin_grid) == 0:
        return []
    elif len(origin_grid) == 1:
        if len(origin_grid[0]) == 1:
            return origin_grid
        if len(origin_grid[0]) > 1:
            # get a copy of original grid
            grid = copy.deepcopy(origin_grid)
            # create a list to store the position of vampire
            vampire_position = []
            # store each posotion as a tuple in a list
            for row_num in range(len(grid)):
                for cell_num in range(len(grid[row_num])):
                    if grid[row_num][cell_num] == 1:
                        vampire_position.append((row_num, cell_num))
            # itenerate over the list of position of vampire
            for posit in vampire_position:
                # update the grid after human adjacent to the posit is vampirized
                grid = vampirize(grid, posit)
            
            # create a new empty list to store the position of healers
            cure_position = []
            # store position as tuple in a list
            for row_num2 in range(len(grid)):
                 for cell_num2 in range(len(grid[row_num])):
                    if grid[row_num2][cell_num2] == 3:
                        cure_position.append((row_num2, cell_num2))
            # cure vampire adjacent to the healer to become a human, itenerate 
            # over the list of positions
            for position in cure_position:
                # update the grid that healers cure adjacent vampires to become
                # human
                grid = cure(grid,position)
            return grid
    else:
        # get a copy of original grid
        grid = copy.deepcopy(origin_grid)
        # create a list to store the position of vampire
        vampire_position = []
        # store each posotion as a tuple in a list
        for row_num in range(len(grid)):
            for cell_num in range(len(grid[row_num])):
                if grid[row_num][cell_num] == 1:
                    vampire_position.append((row_num, cell_num))
        # itenerate over the list of position of vampire
        for posit in vampire_position:
            # update the grid after human adjacent to the posit is vampirized
            grid = vampirize(grid, posit)
            
        # create a new empty list to store the position of healers
        cure_position = []
        # store position as tuple in a list
        for row_num2 in range(len(grid)):
            for cell_num2 in range(len(grid[row_num])):
                if grid[row_num2][cell_num2] == 3:
                    cure_position.append((row_num2, cell_num2))
        # cure vampire adjacent to the healer to become a human, itenerate 
        # over the list of positions
        for position in cure_position:
            # update the grid that healers cure adjacent vampires to become
            # human
            grid = cure(grid,position)
        return grid



def show_city_each_day(grid, day_num):
    '''
    Given a grid and a number of day, print out the situation of the city 
    on the given day. Turn the numbers representing people, vampire, wall or 
    healer to their signs.
    '''
    if len(grid) == 0:
        return -1
    else:
        print('Day {}:\n'.format(day_num))
        for row in grid:
            for cell in row:
                    if cell == 1:
                        print('V', end = ' ')
                    elif cell == 0:
                        print('H', end = ' ')
                    elif cell == 2:
                        print('W', end = ' ')
                    elif cell == 3:
                        print('P', end = ' ')
            print()
        return day_num
    
    
    
def days_remaining_1(grid):
    '''
    Given a matrix representing the city, returns the shortest
    number of days after which there are no humans left in town.
    If the grid is empty or contains only one element which also contains only 
    one element, return -1.
    '''
    
    
    if len(grid) == 0:
        return -1
    elif len(grid) == 1:
        if len(grid[0]) == 1:
            return -1
        if len(grid[0]) > 1:
            num_day = 0 # the starting day
            # make a copy of the original city
            show_city_each_day(grid, num_day)  # show the city on day 0
            original_grid = copy.deepcopy(grid)
            next_grid = next_day(grid)  # get the city on the next day
       
            while next_grid != original_grid:
                # keep looping while next day's city is different from today's
                num_day += 1
                show_city_each_day(next_grid, num_day) # show the city on next day
                original_grid = next_grid # update the original to be current day
                next_grid = next_day(next_grid) # update the next day 
            return num_day
    else:
        num_day = 0 # the starting day
        # make a copy of the original city
        show_city_each_day(grid, num_day)  # show the city on day 0
        original_grid = copy.deepcopy(grid)
        next_grid = next_day(grid)  # get the city on the next day
       
        while next_grid != original_grid:
            # keep looping while next day's city is different from today's
            num_day += 1
            show_city_each_day(next_grid, num_day) # show the city on next day
            original_grid = next_grid # update the original to be current day
            
            
            next_grid = next_day(next_grid) # update the next day 
        return num_day




def days_remaining_2(grid):
    '''
    Given a matrix representing the city, returns the shortest
    number of days after which there are no humans left in town.
    Return -1 if there are humans left.
    '''
    
    
    if len(grid) == 0:
        return -1
    elif len(grid) == 1:
        if len(grid[0]) == 1:
            return -1
        if len(grid[0]) > 1:
            num_day = 0 # the starting day
            # make a copy of the original city
            show_city_each_day(grid, num_day)  # show the city on day 0
            original_grid = copy.deepcopy(grid)
            next_grid = next_day(grid)  # get the city on the next day
        
       
            while next_grid != original_grid:
                # keep looping while next day's city is different from today's
                num_day += 1
                show_city_each_day(next_grid, num_day) # show the city on next day
                original_grid = next_grid # update the original to be current day
        
                next_grid = next_day(next_grid) # update the next day 
        
            # check if there is human in grid
            for row_num in range(len(next_grid)):
                for col_num in range(len(next_grid[row_num])):
                    if next_grid[row_num][col_num] == 0:
                        return -1
            # return number of days when there are no humans        
            return num_day
    else:
        num_day = 0 # the starting day
        # make a copy of the original city
        show_city_each_day(grid, num_day)  # show the city on day 0
        original_grid = copy.deepcopy(grid)
        next_grid = next_day(grid)  # get the city on the next day
        
       
        while next_grid != original_grid:
            # keep looping while next day's city is different from today's
            num_day += 1
            show_city_each_day(next_grid, num_day) # show the city on next day
            original_grid = next_grid # update the original to be current day
        
            next_grid = next_day(next_grid) # update the next day 
        
        # check if there is human in grid
        for row_num in range(len(next_grid)):
            for col_num in range(len(next_grid[row_num])):
                if next_grid[row_num][col_num] == 0:
                    return -1
        # return number of days when there are no humans        
        return num_day





def days_remaining_3(original_grid):
    '''
    Given a matrix representing the city, returns the shortest
    number of days after which there are no humans left in town.
    Returns -1 if not all humans are changed to vampire.
    Stop the simulation after 30 days. Return -1 if there are still humans left.
    '''
    grid = copy.deepcopy(original_grid)
    # return -1 if grid is empty 
    # or has only one element which contains one element
    if len(grid) == 0:
        return -1
    elif len(grid) == 1:
        if len(grid[0]) == 1:
            return -1
        if len(grid[0]) > 1:
            num_day = 0 # the starting day
            # make a copy of the original city
            show_city_each_day(grid, num_day)  # show the city on day 0
        
            # initialize if_healer to check whether healer is in city
            if_healer = 0
            for row_num in range(len(original_grid)):
                for col_num in range(len(original_grid[row_num])):
                    if original_grid[row_num][col_num] == 3:
                        if_healer = 1
            # when healer is in city, stop after 30 days       
            if if_healer == 1: 
                num_day += 1
                next_grid = next_day(grid)  # get the city on the next day
                show_city_each_day(next_grid, num_day)
                while num_day < 30:
                        # keep looping while next day's city is different from today's
                    num_day += 1
                    next_grid = next_day(next_grid) 
                    show_city_each_day(next_grid, num_day) # show the city on next day
            # when there is no healer, runs like days_remaining_2
            if if_healer == 0:
                next_grid = next_day(grid)  # get the city on the next day
                while next_grid != grid:
                     # keep looping while next day's city is different from today's
                     num_day += 1
                     show_city_each_day(next_grid, num_day) # show the city on next day
                     grid = next_grid # update the original to be current day
                     next_grid = next_day(next_grid) # update the next day 
        
            # check if there's still human left
            for row_num in range(len(next_grid)):
                for col_num in range(len(next_grid[row_num])):
                    if next_grid[row_num][col_num] == 0:
                        return -1   
            return num_day
    else:
        num_day = 0 # the starting day
        # make a copy of the original city
        show_city_each_day(grid, num_day)  # show the city on day 0
        
        # initialize if_healer to check whether healer is in city
        if_healer = 0
        for row_num in range(len(original_grid)):
            for col_num in range(len(original_grid[row_num])):
                if original_grid[row_num][col_num] == 3:
                    if_healer = 1
        # when healer is in city, stop after 30 days       
        if if_healer == 1: 
            num_day += 1
            next_grid = next_day(grid)  # get the city on the next day
            show_city_each_day(next_grid, num_day)
            while num_day < 30:
                    # keep looping while next day's city is different from today's
                num_day += 1
                next_grid = next_day(next_grid) 
                show_city_each_day(next_grid, num_day) # show the city on next day
        # when there is no healer, runs like days_remaining_2
        if if_healer == 0:
            next_grid = next_day(grid)  # get the city on the next day
            while next_grid != grid:
                 # keep looping while next day's city is different from today's
                 num_day += 1
                 show_city_each_day(next_grid, num_day) # show the city on next day
                 grid = next_grid # update the original to be current day
                 next_grid = next_day(next_grid) # update the next day 
        
        # check if there's still human left
        for row_num in range(len(next_grid)):
            for col_num in range(len(next_grid[row_num])):
                if next_grid[row_num][col_num] == 0:
                    return -1
            
        return num_day

    