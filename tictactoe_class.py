#################
## Tic-Tac-Toe ##
#################

class TicTacToe:
    def __init__(self):
        self._board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
        self._current_player = 'X'

    def check_for_winner(self) -> bool:
        '''returns True if there is a winning sequence on the board or if
        there is a tie, False otherwise. If there is a tie, updates
        self._current_player to be the string 'tie' for UI purposes'''
        for row in range(3):
            for col in range(3):
                if self._winning_sequence_begins_at((row,col)):
                    return True

        if self._is_tie():
            self._current_player = 'tie'
            return True
        
        return False 
        
    def take_turn(self, move: (int,int)) -> None:
        '''
        writes the X or O on board in the place specified by player's move
        raises an exception if there is already a mark in that space
        '''
        if not self._is_valid_column_number(move[0]) or \
           not self._is_valid_row_number(move[1]):
            raise InvalidMoveError()

        elif self.check_for_winner():
            raise GameOverError()

        elif self._board[move[0]][move[1]] == ' ':
            self._board[move[0]][move[1]] = self._current_player
            if not self.check_for_winner():
                self._switch_player()
        
        else:
            raise ExistingMoveError()
        

    def _switch_player(self) -> None:
        '''changes the current player to be the next player's letter'''
        self._current_player = 'O' if self._current_player == 'X' else 'X'

    def get_board(self) -> [[str]]:
        '''returns the current board'''
        return self._board
    
    def get_current_player(self) -> str:
        '''returns the current player'''
        return self._current_player


    def _is_tie(self) -> bool:
        '''returns True if there is a tie, False otherwise'''
        for row in self._board:
            for col in row:
                if col == ' ':
                    return False
        return True

    def _winning_sequence_begins_at(self, move:(int,int)) -> bool:
        ''' Returns True if a winning sequence of pieces appears on the board
        beginning in the given row and column and extending in any of the
        eight possible directions; returns False otherwise
        '''
        return self._check_three_column(move[0], move[1]) \
            or self._check_three_row(move[0], move[1]) \
            or self._check_three_diagonally(move[0], move[1])

    def _check_three_column(self, move_row: int, move_col:int) -> bool:
        '''returns true if there are three of the same letter in a column'''
        col_list = []
        for row in range(3):
            col_list.append((row, move_col))

        return self._three_in_a_row((move_row, move_col), col_list)


    def _check_three_row(self, move_row: int, move_col:int) -> bool:
        '''returns true if there are three of the same letter in a row'''
        
        row_list = []
        for col in range(3):
            row_list.append((move_row, col))

        return self._three_in_a_row((move_row, move_col), row_list)


    def _check_three_diagonally(self, move_col: int, move_row:int) -> bool:
        '''returns true if there are three of the same letter in a diagonal'''

        return self._three_in_a_row((move_row, move_col),[(0,0), (1,1), (2,2)]) \
               or self._three_in_a_row((move_row,move_col),[(2,0), (1,1), (0,2)])


    def _three_in_a_row(self, player_move:(int,int), potential_three:[(int,int),(int,int),(int,int)]) -> bool:
        '''
        returns True if three boxes on the board in a row/col/diagonal
        are marked with the same letter, False otherwise
        '''
        three = 0
        for potential in potential_three:
            if self._board[player_move[0]][player_move[1]] != ' ' and \
               self._board[potential[0]][potential[1]] == self._board[player_move[0]][player_move[1]]:
                three += 1
                
        return True if three == 3 else False

    def _is_valid_column_number(self, column_number: int) -> bool:
        '''Returns True if the given column number is valid; returns False otherwise'''
        return 0 <= column_number < 3

    def _is_valid_row_number(self, row_number: int) -> bool:
        '''Returns True if the given row number is valid; returns False otherwise'''
        return 0 <= row_number < 3





## Custom Errors

class ExistingMoveError(Exception):
    pass

class InvalidMoveError(Exception):
    pass

class GameOverError(Exception):
    pass
