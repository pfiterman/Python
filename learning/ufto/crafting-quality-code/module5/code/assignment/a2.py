# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType
    
        initialize a Rat with a symbol to show on the maze and its position (row, column)
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        Move the rat's position to the given row and column.
        """
        assert row >= 0, \
               "Invalid row"
        assert col >= 0, \
               "Invalid column"

        self.row = row
        self.col = col

    def eat_sprout(self):
        """ (Rat) -> NoneType

        Increment the number of sprouts ("@") eaten for a rat's instance
        """
        self.num_sprouts_eaten += 1
    
    def __str__(self):
        """ (Rat) -> str

        Return a string representation of the rat object as: "symbol at (row, col) ate num_sprouts_eaten sprouts".    
        """
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of lists of str, Rat, Rat) -> NoneType

        Initialize the game with the maze and two different rats instances

        >>> Maze([['#', '#', '#', '#', '#', '#', '#'], 
                  ['#', '.', '.', '.', '.', '.', '#'], 
                  ['#', '.', '#', '#', '#', '.', '#'], 
                  ['#', '.', '.', '@', '#', '.', '#'], 
                  ['#', '@', '#', '.', '@', '.', '#'], 
                  ['#', '#', '#', '#', '#', '#', '#']], 
                  Rat('J', 1, 1),
                  Rat('P', 1, 4)) 
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = sum(row.count(SPROUT) for row in maze)

        self.maze[rat_1.row][rat_1.col] = rat_1.symbol
        self.maze[rat_2.row][rat_2.col] = rat_2.symbol

    def is_wall(self, row, col):
        """ (Maze, int, int) => boolean

        Return True if and only if there is a wall "#" at the given row and column
        """
        return self.get_character(row, col) == WALL

    def get_character(self, row, col):
        """ (Maze, int, int) => str

        Return the character in the maze at the given row and column. If there is a rat at that location, then its character should be returned rather than HALL
        """
        
        assert 0 <= row < len(self.maze), \
               "Invalid row"
        assert 0 <= col < len(self.maze[0]), \
               "Invalid column"
        
        position = (row, col)
        if position == (self.rat_1.row, self.rat_1.col):
            return RAT_1_CHAR
        elif position == (self.rat_2.row, self.rat_2.col):
            return RAT_2_CHAR
        else:
            return self.maze[row][col]
    
    def move(self, rat, vertical_direction, horizontal_direction):
        """ (Maze, Rat, int, int) => bool

        Move the rat in the given direction, unless there is a wall in the way.
        If there's a Brussels sprout at location make rat eat it (location = HALL and decrease num_sprouts_left)

        Return True if and only if there wasn't a wall in the way. 
        """
        assert vertical_direction in (UP, NO_CHANGE, DOWN), 'Invalid vertical direction.'
        assert horizontal_direction in (LEFT, NO_CHANGE, RIGHT), 'Invalid horizontal direction.'
        
        old_row, old_col = rat.row, rat.col
        new_row = rat.row + vertical_direction
        new_col = rat.col + horizontal_direction
        
        # Test if hit the wall or another rat
        if self.is_wall(new_row, new_col) or \
           self.get_character(new_row, new_col) in (RAT_1_CHAR, RAT_2_CHAR):
           return False
                
        # Remove rat from old square
        self.maze[old_row][old_col] = HALL 
        
        # Is a sprout on the new square? Eat it.   
        if self.get_character(new_row, new_col) == SPROUT:                      
           rat.eat_sprout()
           self.num_sprouts_left -= 1
           self.maze[new_row][new_col] == HALL
        
        # Place rat in the new square and update its location
        self.maze[new_row][new_col] = rat.symbol
        rat.set_location(new_row, new_col)
        
        return True                

    def __str__(self):
        """ (Maze) => str 

        Return a string representation of the maze, using the format shown in this example:
        
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """
        str_maze = ''
        
        for row in self.maze:
            for element in row:
                str_maze += element
            str_maze += '\n'
            
        str_maze += str(self.rat_1) + '\n'
        str_maze += str(self.rat_2) 

        return  str_maze