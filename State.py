import copy
VECTOR = 3

class State():
    def __init__(self, ini_state):  # init
        self.state = ini_state

    def play(self, action, is_expl):  # player:1 - attack, -1 - defensive
        order = self.state[0]
        board = copy.deepcopy(self.state[1])

        x = action[0]
        y = action[1]

        board[x][y] = order

        new_state = [-order, board]

        return State(new_state)

    def is_game_over(self):
        return self.game_result() != 999

    # Return the game result: 1 then the first wins，-1 then the later wins，0 then draw，，999 then the game is not over yet.
    def game_result(self):

        # in rows
        if (self.state[1][0][0] == self.state[1][0][1] == self.state[1][0][2] != 0):
            return self.state[1][0][0]
        elif (self.state[1][1][0] == self.state[1][1][1] == self.state[1][1][2] != 0):
            return self.state[1][1][0]
        elif (self.state[1][2][0] == self.state[1][2][1] == self.state[1][2][2] != 0):
            return self.state[1][2][0]


        # in cols
        if (self.state[1][0][0] == self.state[1][1][0] == self.state[1][2][0] != 0):
            return self.state[1][0][0]
        elif (self.state[1][0][1] == self.state[1][1][1] == self.state[1][2][1] != 0):
            return self.state[1][0][1]
        elif (self.state[1][0][2] == self.state[1][1][2] == self.state[1][2][2] != 0):
            return self.state[1][0][2]

        # Digonal
        if (self.state[1][0][0] == self.state[1][1][1] == self.state[1][2][2] != 0) or (self.state[1][0][2] == self.state[1][1][1] == self.state[1][2][0] != 0):
            return self.state[1][1][1]


        # No one wins so make a choice whether the game is over or continues.
        blank_count = 0
        for i in range(VECTOR):
            for j in range(VECTOR):
                if (self.state[1][i][j] == 0):
                    blank_count += 1
        if blank_count == 0:
            return 0 # Game is over now.
        else:
            return 999 # Continue.


    # Return all possible nodes
    def get_legal_actions(self):
        legal_actions = []
        for i in range(VECTOR):
            for j in range(VECTOR):
                if self.state[1][i][j] == 0:
                    legal_actions.append([i, j])
        return legal_actions