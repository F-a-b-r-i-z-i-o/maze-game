import turtle
import numpy as np


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700, 700)

# Create pen


class Entry(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        wn.addshape('images/entry1.gif')
        self.shape("images/entry1.gif")
        self.penup()
        self.speed(0)


class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        wn.addshape('images/wall-f.gif')
        self.shape('images/wall-f.gif')
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self, walls):
        turtle.Turtle.__init__(self)
        self.walls = walls
        wn.addshape('images/stikerman.gif')
        self.shape('images/stikerman.gif')
        self.penup()
        self.speed(0)

    def go_up(self):
        # calculate move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        # check the space is wall
        if(move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # calculate move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        # check the space is wall
        if(move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # calculate move to
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        # check the space is wall
        if(move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # calculate move to
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        # check the space is wall
        if(move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x, move_to_y)


class Exit(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        wn.addshape('images/exit.gif')
        self.shape('images/exit.gif')
        self.penup()
        self.speed(0)


class Game:
    def __init__(self, labyrinth=None, wall_character=None, agent_character=None, exit_character=None, entry_charachter=None):
        # create wall coordinate
        self.wall = None
        self.player = None
        self.exit = None
        self.entry = None

        self.labyrinth = labyrinth
        self.wall_character = wall_character
        self.agent_character = agent_character
        self.exit_character = exit_character
        self.entry_charachter = entry_charachter

    def create_game(self):
        walls = []
        entry = []
        player_x = 0
        palyer_y = 0

        self.entry = Entry()
        self.wall = Wall()
        self.exit = Exit()

        for y in range(len(self.labyrinth)):
            for x in range(len(self.labyrinth[y])):

                # get the charater at each x,y coordinate
                # Note the order of y and x in the next line
                character = self.labyrinth[y][x]

                # caluclate the screen x, y cooordinates
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)

                if character == self.agent_character:
                    self.entry.goto(screen_x, screen_y)
                    self.entry.stamp()
                    entry.append((screen_x, screen_y))

                # check if it is an X (rapresenting the wall)
                if character == self.wall_character:
                    self.wall.goto(screen_x, screen_y)
                    self.wall.stamp()
                    walls.append((screen_x, screen_y))

                if character == self.agent_character:
                    player_x = screen_x
                    player_y = screen_y

                if character == self.exit_character:
                    self.exit.goto(screen_x, screen_y)

        self.player = Player(walls)
        self.player.goto(player_x, player_y)

    def get_labyrinth(self):
        labyrinth_h = len(self.labyrinth)
        labyrinth_w = len(self.labyrinth[0])

        # initializing the labyrinth
        labyrinth = np.zeros((labyrinth_h, labyrinth_w), dtype=int)

        for y, row in enumerate(self.labyrinth):
            for x, char in enumerate(row):
                if char == self.wall_character:
                    labyrinth[y][x] = 1
                else:
                    labyrinth[y][x] = 0

        return labyrinth
