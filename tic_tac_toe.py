# Game Logic

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Invalid move!')

# User Interface

def get_move():
    row = int(input('Enter the row (0-2): '))
    col = int(input('Enter the column (0-2): '))
    return row, col


def play_game():
    game = TicTacToe()
    while True:
        game.print_board()
        row, col = get_move()
        game.make_move(row, col)

play_game()