import gym
from gym import spaces
import numpy as np

possible_actions = {"U": 0, "D": 1, "L": 2, "R": 3}

actions_id = ["UP", "DOWN", "LEFT", "RIGHT"]

states = {"empty": 0, "wall": 1, "agent": 2, "entry": 3, "exit": 4}

state = {
    "empty": " ",
    "wall": "x",
    "agent": "p",
    "entry": "e",
    "exit": "u",
}


class LabyrinthEnv(gym.Env):
    def __init__(self, max_actions, game=None, map_h=0, map_w=0, load=False):
        """
            map initialization
            map_h (int) height of the maze
            map_w (int) width of the maze
            max_actions (int) max number of actions 
        """
        super(LabyrinthEnv, self).__init__()

        if load:
            self.load_labyrinth()
        else:
            self.map_size = {
                "h": map_h,
                "w": map_w,
            }
            """
            Labyrinth representation
                each cell is
                    0 = empty
                    1 = wall
                    2 = agent
                    3 = entry
                    4 = exit
            """
            self.game = game
            self.labyrinth = self.generate_labyrinth(game)

            self.save_labyrinth()

        self.agent_position = {"x": 1, "y": 1}  # labyrinth entry (1,1)
        self.max_actions = max_actions

        """
            4 possible actions
            Up Down Left Right
        """
        self.action_space = spaces.Discrete(4)
        self.possible_actions = [i for i in range(4)]

        """
            Agent neighborhood
            0 1 2
            3 A 4
            5 6 7

            a list with 8 elements, with int values 0 or 1

            observation can have 2^8=256 possible states
        """
        self.state_space = [i for i in range(256)]

    def save_labyrinth(self):
        """
        Saves the labyrinth to a file as a matrix of int
        """
        np.savetxt("labyrinth", self.labyrinth, delimiter=" ", fmt="%d")

    def load_labyrinth(self):
        """
        Loads the labyrinth from a file
        """
        self.labyrinth = np.loadtxt("labyrinth", delimiter=" ", dtype=int)
        self.map_size = {
            "h": len(self.labyrinth), "w": len(self.labyrinth[0])}
        print(self.map_size)

    def render(self, mode="human"):
        """
        Defines 'obstacles' in the maze and the entry exit and agent
        """

        labyrinth_h = self.map_size["h"]
        labyrinth_w = self.map_size["w"]

        labyrinth_with_info = self.labyrinth.copy()
        labyrinth_with_info[1][1] = 3  # entry
        labyrinth_with_info[labyrinth_h - 2][labyrinth_w - 2] = 4  # exit
        labyrinth_with_info[self.agent_position["y"]][
            self.agent_position["x"]
        ] = 2  # agent

        for y in range(labyrinth_h):
            for x in range(labyrinth_w):
                grid_cell = labyrinth_with_info[y][x]
                if grid_cell == states["wall"]:  # 1
                    print(state["wall"], end="")
                elif grid_cell == states["agent"]:  # 2
                    print(state["agent"], end="")
                elif grid_cell == states["entry"]:  # 3
                    print(state["entry"], end="")
                elif grid_cell == states["exit"]:  # 4
                    print(state["exit"], end="")
                else:  # 0
                    print(state["empty"], end="")
            print("")

    def reset(self):
        """
        Return the agent in the initial position
        """

        self.agent_position = {"x": 1, "y": 1}
        _, observation = self.next_observation()
        return observation

    def state_to_int(self, state):
        """
        Transforms the state list into his binary representation
        Returns the int value of the binary string
        """
        return int("".join(map(str, state)), 2)

    def next_observation(self, action=None):
        """
        Controls the agent's possible actions with the enviroment
        """

        agent_x = self.agent_position["x"]
        agent_y = self.agent_position["y"]
        bumped_wall = False
        if action == possible_actions["U"]:  # 0
            if self.labyrinth[agent_y - 1][agent_x] == 1:
                bumped_wall = True
            else:
                agent_y -= 1
        elif action == possible_actions["D"]:  # 1
            if self.labyrinth[agent_y + 1][agent_x] == 1:
                bumped_wall = True
            else:
                agent_y += 1
        elif action == possible_actions["L"]:  # 2
            if self.labyrinth[agent_y][agent_x - 1] == 1:
                bumped_wall = True
            else:
                agent_x -= 1
        elif action == possible_actions["R"]:  # 3
            if self.labyrinth[agent_y][agent_x + 1] == 1:
                bumped_wall = True
            else:
                agent_x += 1

        self.agent_position["x"] = agent_x
        self.agent_position["y"] = agent_y

        """
        if the agent wants to move to a free position
        it moves it and calculates the next observation in the form of integer
        """

        state = [
            self.labyrinth[agent_y - 1][agent_x - 1],  # 0
            self.labyrinth[agent_y - 1][agent_x],  # 1
            self.labyrinth[agent_y - 1][agent_x + 1],  # 2
            self.labyrinth[agent_y][agent_x - 1],  # 3
            self.labyrinth[agent_y][agent_x + 1],  # 4
            self.labyrinth[agent_y + 1][agent_x - 1],  # 5
            self.labyrinth[agent_y + 1][agent_x],  # 6
            self.labyrinth[agent_y + 1][agent_x + 1],  # 7
        ]

        return bumped_wall, self.state_to_int(state)

    def step(self, action: int, draw=False):
        """
        Function to move the agent in the map
        """

        if draw:
            if action == possible_actions["U"]:  # 0
                self.game.player.go_up()
            elif action == possible_actions["D"]:  # 1
                self.game.player.go_down()
            elif action == possible_actions["L"]:  # 2
                self.game.player.go_left()
            elif action == possible_actions["R"]:  # 3
                self.game.player.go_right()

        bumped_wall, observation = self.next_observation(action)
        reward = -1
        done = False

        if bumped_wall:
            reward = -5

        if (
            self.agent_position["x"] == self.map_size["w"] - 2
            and self.agent_position["y"] == self.map_size["h"] - 2
        ):
            done = True
            reward = 10

        self.max_actions = self.max_actions - 1
        if self.max_actions == 0:
            done = True

        return observation, reward, done, {}

    def generate_labyrinth(self, game=None):
        """
        Function that generate the labyrint
        """

        if game is not None:
            return game.get_labyrinth()

    def action_space_sample(self):
        """
        Function to random move the agent
        """
        return np.random.choice(self.possible_actions)
