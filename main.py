import numpy as np
VECTOR = 3  # a 3x3 grid
from State import State
from Node import Node


if __name__ == '__main__':
    # init
    state = np.zeros([VECTOR, VECTOR])
    order = 1
    state = State([order, state])
    first = 'player'  # 'player' -   'ai' -
    status = 999


    while status == 999 :
        if first == 'player':
            for i in state.state[1]:
                print(i)

            player_choice = [int(i) for i in input('input the loacation (x,y):').split(',')]
            state = state.play(player_choice, 0)
            print('player:', player_choice)

            state = State([state.state[0], state.state[1]])
            for i in state.state[1]:
                print(i)

            if state.game_result() == 0 or state.game_result() == 1 or state.game_result() == -1:
                status = state.game_result()
                break


            tree = Node(state)
            ai_choice = tree.best_action().parent_action
            state = state.play(ai_choice, 0)
            state = State([state.state[0], state.state[1]])

            print('ai:', ai_choice)

        else:
            state = State([state.state[0], state.state[1]])
            tree = Node(state)

            ai_choice = tree.best_action().state.state[1][-1]
            state = state.play(ai_choice, 0)

            print('ai:', ai_choice)

            for i in state.state[1]:
                print(i)

            player_choice = [int(i) for i in input('input the loacation (x,y):').split(',')]
            state = state.play(player_choice, 0)
            print('player:', player_choice)

            for i in state.state[1]:
                print(i)

        status = state.game_result()



    if status == 1:
        print('Great! You won the game!')
    elif status == -1:
        print('Unfortunately, you lost.')
    elif status == 0 :
        print('You draw.')