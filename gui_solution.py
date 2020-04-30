import tkinter
import tictactoe_class
import point

class TicTacToeGUI:
    def __init__(self):
        self._root_window = tkinter.Tk()

        self._game = tictactoe_class.TicTacToe()


        self._turn_text = tkinter.StringVar()
        self._turn_text.set(self._turn_or_win())
        
        turn = tkinter.Label(master = self._root_window,
                                   textvariable = self._turn_text)
        turn.grid(row = 0, column = 0, padx = 10, pady = 10,
                        sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas = tkinter.Canvas(master = self._root_window,
                                      width = 500, height = 400,
                                      background = '#ccccff')
        self._canvas.grid(row = 1, column = 0,
                          sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def start(self) -> None:
        '''activates GUI and hands over control to tkinter'''
        self._root_window.mainloop()

    def _turn_or_win(self) -> str:
        '''returns string describing whose turn/win it is'''        
        if not self._game.check_for_winner():
            text = "{}'s Turn".format(self._game.get_current_player())
        else:
            winner = self._game.get_current_player()
            if winner == 'tie':
                text = "It's a tie!"
            else:
                text = "{} Wins!".format(winner)

        return text

    def _get_canvas_dimensions(self) -> (int,int):
        '''returns current width and height of canvas'''
        
        return self._canvas.winfo_width(), self._canvas.winfo_height()

    def _on_canvas_clicked(self, event:tkinter.Event) -> None:
        '''generates a event.x and event.y coordinate to determine where
        the click occured and then calls the appropriate functions to redraw
        the board with the letter created by the click if the move is legal'''
        
        width, height = self._get_canvas_dimensions()

        click_point = point.from_pixel(
            (event.x, event.y), (width, height))

        self._handle_click(click_point)
        self._turn_text.set(self._turn_or_win())

        self._draw_board()

    def _handle_click(self, click_point: point.Point) -> None:
        '''runs functions to determine if a valid tictactoe move'''
        try:
            self._game.take_turn(self._get_square(click_point))
            if not self._game.check_for_winner():
                self._game.switch_players()

        except:
            pass

    def _get_square(self, click_point: point.Point) -> (int,int):
        '''returns row and column of the board where board was clicked'''
        point_x, point_y = click_point.frac()
        
        for n in range(3):
            upper = (n+1)/3
            lower = n/3

            if lower < point_y < upper:
                click_row = n
                
            if lower < point_x < upper:
                click_col = n

        return click_row, click_col


    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''when canvas is resized, redraws board to fit to window'''
        self._draw_board()

    def _draw_board(self) -> None:
        '''draws the current board'''
        self._canvas.delete(tkinter.ALL)

        width, height = self._get_canvas_dimensions()
        
        self._draw_grid(width, height)
        self._draw_letters(width, height)

    def _draw_grid(self, canvas_width, canvas_height) -> None:
        '''draws the grid created by dividing the canvas into rows/columns'''
        for row in range(2):
            self._canvas.create_line(
                0, (canvas_height * ((1 + row) / 3)),
                canvas_width, (canvas_height * ((1 + row) / 3)))

        for col in range(2):
            self._canvas.create_line(
                (canvas_width * ((1 + col) / 3)), 0,
                (canvas_width * ((1 + col) / 3)), canvas_height)

    def _draw_letters(self, canvas_width, canvas_height) -> None:
        '''draws any letters currently on the board'''
        board = self._game.get_board()
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'O':
                    self._canvas.create_oval(
                        (canvas_width * ((col) / 3)), (canvas_height * (row/3)),
                        (canvas_width * ((1+col)/3)), (canvas_height * ((row+1)/3)),
                        outline = 'black')
                    
                elif board[row][col] == 'X':
                    #draw \
                    self._canvas.create_line(
                        (canvas_width * (col / 3)), (canvas_height * (row/3)),
                        (canvas_width * ((1+col)/3)), (canvas_height * ((row+1)/3)))
                    #draw /
                    self._canvas.create_line(
                        (canvas_width * (col / 3)), (canvas_height * ((row+1)/3)),
                        (canvas_width * ((1+col)/3)), (canvas_height * (row/3)))
                                                     



if __name__ == '__main__':
    game = TicTacToeGUI()
    game.start()
        
