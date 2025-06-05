class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()

class Board:
    valid_moves = ["upper left", "upper center", "upper right", "middle left", "middle center", "middle right", "bottom left", "bottom center", "bottom right"]
    def __init__(self):
        self.board_array = [['']] * 3 for in range(3)]
        self.turn = 'x'

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append('-----------\n')
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append('-----------\n')
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return ''.join(lines)
    
    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That move is invalid")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3
        if self.board_array[row][column] != '':
            raise TictactoeException("That space is already used")
        self.board_array[row][column] = self.turn
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def whats_next(self):
        cat_game = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == ' ':
                    cat_game = False
                else:
                    continue
                break
            else:
                continue
            break
        if (cat_game):
            return (True, 'Cats Game')
        won_game = False
        for i in range(3):
            if self.board_array[i][0] != ' ':
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    won_game = True
                    break
        if not won_game:
            for i in range(3):
                if self.board_array[0][i] != ' ':
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        won_game = True
                        break
        if not won_game:
            if self.board_array[1][1] != ' ':
                if self.board_array[0][0] == self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    won_game = True
                if self.board_array[0][2] == self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    won_game = True
        if not won_game:
            if self.turn == 'X':
                return (False, 'X turn')
            else:
                return (False, 'O turn')
        else:
            if self.turn == 'O':
                return (True, 'X wins!')
            else:
                return (True, 'O wins!')

    While True:
        board = Board()
        while True:
            state = board.whats_next()
            if not state[0]:
                print(board)
                while True:
                    print(f"Valid moves are: {Board.valid_moves}")
                    print(state[1])
                    user_input = input("Select where to place your symbol: ")
                    try:
                        board.user_input(user_input)
                        break
                    except TictactoeException as e:
                        print(e.message)
                continue
            else:
                print(board)
                print(state[1])
                break

        play_again = input('Enter yes to play again')
        if play_again != 'yes':
            break

