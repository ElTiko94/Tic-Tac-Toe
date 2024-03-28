import random

class QLearningAgent:
    def __init__(self, epsilon=0.1, alpha=0.5, gamma=0.9):
        self.q_values = {}  # Dictionary to store Q-values
        self.epsilon = epsilon  # Exploration rate
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.last_state = None
        self.last_action = None

    def get_q_value(self, state, action):
        return self.q_values.get((state, action), 0.0)

    def update_q_value(self, state, action, reward, next_state):
        best_next_action = max(self.get_possible_actions(next_state), key=lambda a: self.get_q_value(next_state, a))
        td_target = reward + self.gamma * self.get_q_value(next_state, best_next_action)
        td_delta = td_target - self.get_q_value(state, action)
        self.q_values[(state, action)] = self.get_q_value(state, action) + self.alpha * td_delta

    def choose_action(self, state, possible_actions):
        if random.random() < self.epsilon:
            return random.choice(possible_actions)
        else:
            return max(possible_actions, key=lambda a: self.get_q_value(state, a))

    def get_possible_actions(self, state):
        return [action for action in range(9) if state[action] == ' ']