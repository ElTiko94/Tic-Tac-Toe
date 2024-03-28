from q_learning_agent import QLearningAgent
import pickle

def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    winning_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for condition in winning_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def get_reward(board, player):
    if check_winner(board, player):
        return 1
    else:
        return 0

def get_state(board):
    return tuple(board)

def main():

    try:
        with open("object.pkl", "rb") as f:
            agent = pickle.load(f)
    except FileNotFoundError:
        agent = QLearningAgent()

    agent2 = QLearningAgent()
    x_count = 0
    o_count = 0

    print("Welcome to Tic Tac Toe!")

    itteration = 0

    while True:
        board = [' '] * 9
        current_player = 'X'
        print_board(board)
        print("")
        moves = 1

        while True:
            state = get_state(board)
            if current_player == 'X':
                action = agent2.choose_action(state, agent2.get_possible_actions(state))
                
            else:
                action = agent.choose_action(state, agent.get_possible_actions(state))

            row = action // 3
            col = action % 3
            board[action] = current_player

            print_board(board)
            print("")

            reward = get_reward(board, current_player)
            if reward != 0:
                agent.update_q_value(agent.last_state, agent.last_action, reward, get_state(board))
                if reward == 1:
                    print("Player X wins!" if current_player == 'X' else "Player O wins!")
                    if current_player == 'X':
                        x_count +=1
                    else:
                        o_count +=1
                break
            elif  moves == 9:
                if reward == 1:
                    print("Player X wins!" if current_player == 'X' else "Player O wins!")
                    if current_player == 'X':
                        x_count +=1
                    else:
                        o_count +=1
                else :
                    print("It's a draw!")
                break

            moves += 1
            agent.update_q_value(agent.last_state, agent.last_action, reward, get_state(board))

            current_player = 'X' if current_player == 'O' else 'O'

        play_again = "yes" #input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            with open("object.pkl", "wb") as file:
                pickle.dump(agent, file)
            break
        itteration += 1
        if itteration > 1000:
            with open("object.pkl", "wb") as file:
                pickle.dump(agent, file)
            break

    print (f"X wins {x_count} times")
    print (f"O wins {o_count} times")

if __name__ == "__main__":
    main()
