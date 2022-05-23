import turtle
import numpy as np

# Write screen to play game

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700, 700)


# Define class to write the entry

class Entry(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        wn.addshape('images/entry1.gif')
        self.shape("images/entry1.gif")
        self.penup()
        self.speed(0)


# Define class to write the wall

class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        wn.addshape('images/wall-f.gif')
        self.shape('images/wall-f.gif')
        self.penup()
        self.speed(0)

# Define class to write the player


class Player(turtle.Turtle):
    def __init__(self, walls):
        turtle.Turtle.__init__(self)
        self.walls = walls
        wn.addshape('images/stikerman.gif')
        self.shape('images/stikerman.gif')
        self.penup()
        self.speed(0)

    """
    Define the possible action of the player
    """

    def go_up(self):
        # calculate move to in the map
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        # check the space is wall
        if(move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # calculate move to in the map
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        # check the space is wall
        if(move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # calculate move to in the map
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        # check the space is wall
        if(move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # calculate move to in the map
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        # check the space is wall
        if(move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x, move_to_y)

# Define the class for the exit


class Exit(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        wn.addshape('images/exit.gif')
        self.shape('images/exit.gif')
        self.penup()
        self.speed(0)

# Define the class for the map


class Game:
    def __init__(self, map=None, wall_character=None, agent_character=None, exit_character=None, entry_charachter=None):

        # inizalizate the wall
        self.wall = None

        # inizializate the player
        self.player = None

        # inizializate the exit
        self.exit = None

        # inizializate the entry
        self.entry = None

        # inizlizate the map
        self.map = map

        # define wall character
        self.wall_character = wall_character

        # define agent character
        self.agent_character = agent_character

        # define exit caracter
        self.exit_character = exit_character

        # define the entry character
        self.entry_charachter = entry_charachter

    """
    Principal function to create the GUI interface of the game
    """

    def create_game(self):
        walls = []
        entry = []
        player_x = 0
        player_y = 0

        self.entry = Entry()
        self.wall = Wall()
        self.exit = Exit()

        for y in range(len(self.map)):
            for x in range(len(self.map[y])):

                # get the charater at each x,y coordinate
                # Note the order of y and x in the next line
                character = self.map[y][x]

                # caluclate the screen x, y cooordinates
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)

                # check if it is a character rapresenting the agent
                if character == self.agent_character:
                    self.entry.goto(screen_x, screen_y)
                    self.entry.stamp()
                    entry.append((screen_x, screen_y))

                # check if it is a character rapresenting the wall
                if character == self.wall_character:
                    self.wall.goto(screen_x, screen_y)
                    self.wall.stamp()
                    walls.append((screen_x, screen_y))

                # position the agent in the map
                if character == self.agent_character:
                    player_x = screen_x
                    player_y = screen_y

                # check if it is a character rapresenting the exit
                if character == self.exit_character:
                    self.exit.goto(screen_x, screen_y)
        # write wall
        self.player = Player(walls)
        # write player
        self.player.goto(player_x, player_y)

    """
    Function to transform map in 0 1 rapresentation
    """

    def get_labyrinth(self):
        map_h = len(self.map)
        map_w = len(self.map[0])

        map = np.zeros((map_h, map_w), dtype=int)

        for y, row in enumerate(self.map):
            for x, char in enumerate(row):
                if char == self.wall_character:
                    map[y][x] = 1
                else:
                    map[y][x] = 0

        return map
