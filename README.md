# maze-game

<hr>

## Project Description

Design and implementation of a reinforcement learning environment, for training an agent using a Q-Learning algorithm in the framework of AI-Gym.

**Goal**

<br>

The purpose of the project is to show that the agent, through reinforcement learning, can learn to move in the labyrinth without bumping on the walls.

**Environment**

<br>

A mxn grid of cells where each cells is either empty (white) or a wall (coloured), where the agent is located in a upper left position (es. cell 2,2 in figure) and the exit is lower rigth position and certain percentage of random walls cells represent the labyrinth.

**Agent**

<br>

The agent available action are the four movement actions: Up, Down, Left, Right.

**State**

The percept state returned from the environment is a representation of the Moore 8-neighborhood centered in agent position.

**Actions effect**

Each actions has the effect of moving the corresponding position of the agent in the environment and returning the appropriate state and reward.
Moving toward a wall causes the agent bumping in the wall without changing position

<br>

**Reward**
Each movement action has a reward of -1, bumping toward a wall has a reward of -5 reaching the final exit position has a reward of 10.

<br>

**Stop condition**

the agent reach the exit cell or maxK actions are executed.

<br>

## implementation

<hr>

The implementation of the environment have:

- m, n dimensions of the grid.

- percentage of walls

- maxK maximum number of actions before end

<br>

The system have:

- Run and train the Qlearning reinforcement learning algorithm,
- Generating and trying different labirinths during training, showing the evolution of the accumulated reward
- Saving the Q(State, Action) matrix, Loading a saved Q matrix
- Executing the agent step-by-step on a given labirynth showing the reward
