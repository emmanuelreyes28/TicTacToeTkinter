#Emmanuel Reyes 58725927
#game_logic

directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1, -1), (-1,0), (-1, 1)]

class OthelloGameState:
    def __init__(self, rows: int, cols: int, turn: str, top_left: str, mode: str):
        self.board = []
        for row in range(rows):
            row_list = []
            for col in range(cols):
                row_list.append('.')
            self.board.append(row_list)
            
        c_row = int(rows/2)
        c_col = int(cols/2)
        if top_left == 'B':
            self.board[c_row - 1][c_col - 1] = 'B' #top left
            self.board[c_row - 1][c_col] = 'W' 
            self.board[c_row][c_col -1] = 'W'
            self.board[c_row][c_col] = 'B'
            
        elif top_left == 'W':
            self.board[c_row - 1][c_col - 1] = 'W' #top left
            self.board[c_row - 1][c_col] = 'B' 
            self.board[c_row][c_col -1] = 'B'
            self.board[c_row][c_col] = 'W'

        self.row = rows
        self.cols = cols
        self.white = 'W'
        self.black = 'B'
        self.turn = turn
        self.mode = mode
            

    def print_board(self):
        for thing in self.board:
            print(' ')
            for dot in thing:
                print(dot, end = ' ')

    def check_all(self, row:int, col:int):
        empty_list = []
        for x,y in directions:
            
            row_copy = row #row -1 col -1
            col_copy = col
            row_copy += x
            col_copy += y
            try:
                if self.board[row_copy][col_copy] != '.':
                    print()
                    row_copy += x
                    col_copy += y
                    while self.board[row_copy][col_copy] == self.opposite_color():
                        row_copy += x
                        col_copy += y
                    if self.board[row_copy][col_copy] == self.turn:
                        
                        while True:
                            row_copy -= x
                            col_copy -= y
                            if row_copy == row and col_copy == col:
                                break
                            empty_list.append((row_copy, col_copy)) # add the coordinates to flip the list
                    else:
                        return empty_list 
                          
                                    
            except IndexError:
                pass
        return empty_list

    def move(self, row:int, col:int):
        check_dir = self.check_all(row, col)
        if check_dir == []:
            print('INVALID')
        elif self.board[row][col] != '.':
            print('INVALID')
        else:
            self.board[row][col] = self.turn
            for x,y in check_dir:
                self.board[x][y] = self.turn 
        
                        
       
    def opposite_color(self):
        if self.turn == self.white:
            return self.black
        else:
            return self.white

    def score_board(self):
        white = 0
        black = 0
        for row in self.board:
            for col in row:
                if col == self.white:
                    white += 1
                elif col == self.black:
                    black += 1
        self.w_score = white
        self.b_score = black
        return('B: {} W: {}'.format(self.b_score, self.w_score))

    def _turn(self):
        if self.turn == self.black:
            return self.white
            print('Turn: White')
            #self.turn = self.white
        else:
            #self.turn = self.black:
            return self.black
            print('Turn: Black')

    def winner(self):
        if self.mode == '<':
            if self.w_score < self.b_score:
                print('WINNER: WHITE')
            elif self.b_score < self.w_score:
                print('WINNER: BLACK')
            else:
                print('WINNER: NONE')
        else:
            if self.w_score > self.b_score:
                print('WINNER: WHITE')
            elif self.b_score > self.w_score:
                print('WINNER: BLACK')
            else:
                print('WINNER: NONE')
     
                               
if __name__ == '__main__':
    o = OthelloGameState(4, 4, 'B', 'B', '<')
    o.print_board()
    print()
    o.move(3,3)
    o.score_board()
    o.print_board()
    
