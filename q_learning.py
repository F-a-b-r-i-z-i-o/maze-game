import numpy as np
import time
import map_env
import matplotlib.pyplot as plt


class QLearning(object):
    def __init__(self, env):
        self.env = env
        self.obs = None
        self.tot_reward = 0

    def max_action(self, q, state, actions):
        """
        Returns the actions with highest value in the Q matrix for a given state
        """
        values = np.array([q[state, a] for a in actions])
        action = np.argmax(values)
        return actions[action]

    def save_q(self, q, file_name):
        """
        Saves the Q matrix to a file
        """
        num_states = len(self.env.state_space)
        num_actions = len(self.env.possible_actions)
        q_matrix = np.zeros((num_states, num_actions))
        x = 0
        for state in self.env.state_space:
            y = 0
            for action in self.env.possible_actions:
                q_matrix[x][y] = q[state, action]
                y += 1
            x += 1
        np.savetxt(file_name, q_matrix, delimiter=" ")

    def load_q(self, file_name):
        """
        Loads the Q matrix from a file
        """
        q = {}
        for state in self.env.state_space:
            for action in self.env.possible_actions:
                q[state, action] = 0
        with open(file_name) as file_name:
            q_matrix = np.loadtxt(file_name, delimiter=" ")

        x = 0
        for state in self.env.state_space:
            y = 0
            for action in self.env.possible_actions:
                q[state, action] = q_matrix[x][y]
                y += 1
            x += 1
        return q

    def execute(self, step_by_step=False):
        """
        Executes the Q-Learning algorithm from the matrix saved step by step
        """
        self.env.reset()
        self.env.render()
        q = self.load_q("Qmatrix")
        tot_reward = 0

        command = ""
        print("Command List")
        while command != "n":
            if step_by_step:
                print("------------------------")
                print("Turn left: l")
                print("Turn right: r")
                print("Up: u")
                print("Down: d")
                print("------------------------")
                command = input()
            else:
                time.sleep(0.5)

            _, self.obs = self.env.next_observation()

            if command == "u":
                action = map_env.possible_actions["U"]
            elif command == "d":
                action = map_env.possible_actions["D"]
            elif command == "l":
                action = map_env.possible_actions["L"]
            elif command == "r":
                action = map_env.possible_actions["R"]
            else:  # y
                action = self.max_action(
                    q, self.obs, self.env.possible_actions)

            observation_next, reward, done, info = self.env.step(
                action, draw=True)
            self.tot_reward += reward

            self.env.render()
            print("Action:\t" + map_env.actions_id[action])
            print("Reward:\t{}".format(reward))
            print("Return:\t{}".format(str(self.tot_reward)))
            print("")

            if done:
                print("")
                print("The Agent has reached the exit")
                input("")

    def training(
        self, epochs=25000, steps=200, alpha=0.1, gamma=1.0, eps=1.0, plot=True
    ):
        """
        Trains the Q-Learning Algorithm and saves the Q matrix built
        Default hyperparameters
            alpha = 0.1 is the learning rate of q learning
            gamma = 1.0 is the discount factor
            eps = 1.0   is the epsilon and is related to the greedy value of the algorithm
            epochs = 50000 is the max number of epochs
            steps = 200 is the max number of actions ( step ) per epoch
        """
        # initializing Q(state, action) matrix to zero
        q = {}
        for state in self.env.state_space:
            for action in self.env.possible_actions:
                q[state, action] = 0

        self.env.reset()
        self.env.render()

        total_rewards = np.zeros(epochs)
        start_time = time.time()

        for i in range(epochs):
            if i % int(epochs / 10) == 0:
                print("epochs passed: ", i)

            done = False
            ep_rewards = 0
            num_actions = 0
            observation = self.env.reset()
            while not done and num_actions <= steps:
                rand = np.random.random()
                action = (
                    self.max_action(q, observation, self.env.possible_actions)
                    if rand < (1 - eps)
                    else self.env.action_space_sample()
                )
                observation_next, reward, done, info = self.env.step(action)
                num_actions += 1
                ep_rewards += reward
                action_next = self.max_action(
                    q, observation_next, self.env.possible_actions
                )
                q[observation, action] = q[observation, action] + alpha * (
                    reward
                    + gamma * q[observation_next, action_next]
                    - q[observation, action]
                )
                observation = observation_next
            if eps - 2 / epochs > 0:
                eps -= 2 / epochs
            else:
                eps = 0
            total_rewards[i] = ep_rewards

        end_time = time.time()

        if plot:
            plt.plot(total_rewards)
            plt.show()

        self.save_q(q, "Qmatrix")

        print("execution time = {:.2f} seconds".format(end_time - start_time))
