import pygame
from colors import Color

class Grid:
    def __init__(self):
        self.num_row = 20
        self.num_col = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_col)] for i in range(self.num_row)]
        self.colors = Color.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_row):
            for column in range(self.num_col):
                print(self.grid[row][column],end=" ")
            print()   
    
    def is_inside(self,row,column):
        if row >= 0 and row < self.num_row and column >=0 and column < self.num_col:
            return True
        return False





    def draw(self,screen):
        for row in range(self.num_row):
            for column in range(self.num_col):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +1 ,row*self.cell_size +1 ,self.cell_size -1 ,self.cell_size-1)
                pygame.draw.rect(screen,self.colors[cell_value],cell_rect)