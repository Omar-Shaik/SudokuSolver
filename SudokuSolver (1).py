#!/usr/bin/env python
# coding: utf-8

# In[17]:


"""
We dont need to include a test to ensure we have the correct number placement due to the way the
algorithm is set up; so we can assume once the board is filled we have reached our solution.
If we ever reach a position where the solution is not valid we will backtrack.
This function returns a boolean value relating to if we found the solution or not
"""
from sudokugen.generator import generate, Difficulty
import numpy as np


def solve1(bo):
    # print(bo)  # for testing and visualization purposes
    # Base case of our recursion
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    # Loop through values 1-9, and check if adding those into the board will be a valid solution
    for i in range(1, 10):
        # intakes value of board, num, and the position of empty square as [row][col] if valid
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            # recursively try to finish the solution by calling solve on our new board
            if solve1(bo):
                return True
            # if we cannot find solution based on value added; we need to reset and try a different
            # value and repeat the recursive process
            bo[row][col] = 0
    return False


# checks if play/number is valid at the position
def valid(bo, num, pos):
    # check row entered as [row][column]
    for i in range(len(bo[0])):
        """
        Check through each element in the row, and check if it is equal to the number
        we have just inserted, we also disregard the position of the inserted number
        as by logic, it will be true at that position.
        """
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(bo)):
        # Same logic as above
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    """
    check which 3x3 box, we are in using integer division
    given a position, we will determine which mini-square it is in
    the y position will be {0, 1, 2} and the x {0, 1, 2}
    the variables will give us a value between 0-2
    """

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Loop through all 9 elements in the box to ensure we dont have the same element appearing twice
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    # If we make it past all the checks than it is a valid position for the number
    return True


# Not my function, may use a built in library to generate readable results
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


# Given a board, find an empty square on board at position[i][j] and return position of the square
# if no blank square return none, which will trigger the Solve function
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

board = generate(difficulty=Difficulty.HARD) 
arr = np.array(board[0])
matrix = np.reshape(arr, (9, 9))
matrix2 = np.reshape(arr, (9, 9))
print("Generated Puzzle")
print(matrix)
solve1(matrix)
print("\nSolved Puzzle")
print(matrix)











# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




