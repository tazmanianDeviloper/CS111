#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#
import string


class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for _ in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''  # begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'  # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # add your code here ###
        for j in range(self.width):
            s += '--'
        s += '\n'
        for i in range(self.width):
            i %= 10
            s += str(i) + ' '
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert (checker == 'X' or checker == 'O')
        assert (0 <= col < self.width)

        # put the rest of the method here ###
        for dept in range(-1, self.height * -1 - 1, -1):
            if self.slots[dept][col] != 'X' and self.slots[dept][col] != 'O':
                self.slots[dept][col] = checker
                break

    # add your reset method here ###

    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: columns is a string of valid column numbers
        """
        checker = 'X'  # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    # add your remaining methods here
