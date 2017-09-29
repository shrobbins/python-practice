"""
Clone of 2048 game. - Sue
"""
#http://www.codeskulptor.org/#user43_LilOVE2chf_29.py
import poc_2048_gui
#import user43_zxf3vhXitr_5 as board_2048_testsuite
import random


# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4


# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    list1 = remove_zeros(line)
    list2 = merge_tiles(list1)
    list3 = remove_zeros(list2)
    return list3
    
            
def remove_zeros(merge_list):
    """
    Function that appends zeros to the end of line.
    """
    
    zero_list = []
    result = []
    for index in range(len(merge_list)):
        if merge_list[index] > 0:
            result.append(merge_list[index])
        else:
            zero_list.append(merge_list[index])
    result.extend(zero_list)
    return result
    
def merge_tiles(tile_list):
    """
    Function that merges tiles so they double in value.
    """
    
    result2 = [0] * len(tile_list) 
    for index in range(len(tile_list)):
        if index == 0:
            result2[index] = tile_list[index]
        elif tile_list[index] > 0 and tile_list[index] == tile_list[index-1]:
            result2[index-1] = tile_list[index] + tile_list[index-1]
            tile_list[index] = 0 
        else:
            result2[index] = tile_list[index]
    return result2 

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
               
        start_cells_up = []
        start_cells_down = []
        start_cells_left = []
        start_cells_right = []
        
        self._init_dict = {UP: start_cells_up,
             DOWN: start_cells_down,
             LEFT: start_cells_left,
             RIGHT: start_cells_right}

        for col in range(self.get_grid_width()):
            start_cells_up.append( (0, col) )
            start_cells_down.append( (self.get_grid_height()-1, col) )
        for row in range(self.get_grid_height()):
            start_cells_left.append( (row, 0) )
            start_cells_right.append( (row, self.get_grid_width()-1) ) 
            
            
        
       
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # Create a rectangular grid using nested list comprehension
        self._board_grid = [[0 for dummy_col in range(self._grid_width)]
                           for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()
         
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return  "\n".join([str(row) for row in self._board_grid])
       

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height
        

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width
        

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
          
        def traverse_grid(start_cell, movement, num_steps):
            """
            Function that iterates through the cells in a grid
            in a linear direction
    
            Both start_cell is a tuple(row, col) denoting the
            starting cell
    
            direction is a tuple that contains difference between
            consecutive cells in the traversal
            """
             
            tile_tuple = []
            tile_value = []
            for step in range(num_steps):
                row = start_cell[0] + step * movement[0]
                col = start_cell[1] + step * movement[1]
                tile_tuple.append((row, col))
                tile_value.append(self._board_grid[row][col])
            merged_tiles = merge(tile_value)
            
            
            
            for index in range(len(tile_tuple)):
                for number in range(len(merged_tiles)):
                    if index == number:
                        self.set_tile(tile_tuple[index][0], tile_tuple[index][1], merged_tiles[number])
            
             
            
        self.check_board(self._board_grid)  
        
        if direction == 1:
                for tile in self._init_dict[1]:
                    
                    traverse_grid(tile, (OFFSETS[1][0], OFFSETS[1][1]), self.get_grid_height()) 
        elif direction == 2:
                for tile in self._init_dict[2]:
                    traverse_grid(tile, (OFFSETS[2][0], OFFSETS[2][1]), self.get_grid_height())            
        elif direction == 3:
               for tile in self._init_dict[3]:
                    traverse_grid(tile, (OFFSETS[3][0], OFFSETS[3][1]), self.get_grid_width())
        else:
               for tile in self._init_dict[4]:
                    traverse_grid(tile, (OFFSETS[4][0], OFFSETS[4][1]), self.get_grid_width())
            
        if self._grid_copy != self._board_grid:
                self.new_tile()
        
                                       

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        grid_with_zeros = []
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                if self._board_grid[row][col] == 0:
                    grid_with_zeros.append( (row,col))
        new_square = random.choice(grid_with_zeros)
        
       
        
        def random_tile():
            """
            Create a random tile of 2 or 4
            """
            if random.random() >= 0.1:
                value = 2
            else:
                value = 4
            sq_val = value
            return sq_val
                    
        self.set_tile(new_square[0], new_square[1], random_tile())
        
        
                          
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board_grid[row][col] = value
         

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return  self._board_grid[row][col]
    
    
    def check_board(self, grid):
        """
        Return copy of grid before move function.
        """
        self._grid_copy = [item[:] for item in grid] 
        return self._grid_copy
        
        


poc_2048_gui.run_gui(TwentyFortyEight(4, 5))
#board_2048_testsuite.run_suite(TwentyFortyEight)