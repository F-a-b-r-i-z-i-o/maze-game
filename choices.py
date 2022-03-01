import utils
import sys
from map_env import LabyrinthEnv
from game import Game
from q_learning import QLearning
import level


def main_menu():
    choice = '0'
    while choice == '0':
        print("")
        print("Choose the level you want to play:\n")
        print("(1)\tMap 10 x 10\n")
        print("(2)\tMap 20 x 20\n")
        print("(3)\tMap 30 x 30\n")
        print("(4)\tExit Game\n")

        choice = input("\tPlease make a choice:\n ")

        if choice == "1":
            print("-----------------------------------------")
            print("\tLEVEL 1 SELECTED\n")
            print("-----------------------------------------")
            lev1_menu()
        elif choice == "2":
            print("-----------------------------------------")
            print("\tLEVEL 2 SELECTED\n")
            print("-----------------------------------------")
            lev2_menu()
        elif choice == "3":
            print("-----------------------------------------")
            print("\tLEVEL 3 SELECTED\n")
            print("-----------------------------------------")
            lev3_menu()
        elif choice == "4":
            print("-----------------------------------------")
            print("\tEXIT GAME\n")
            print("-----------------------------------------")
            sys.exit()
        else:
            print("I don't understand your choice.")


def lev1_menu():
    wall_input = input(
        "Choose the percentage of the wall:\n"
        "(1)\tLow\n"
        "(2)\tMedium\n"
        "(3)\tHigh\n"
    )

    env = None

    if wall_input == "1":
        max_actions = int(input("\tMax actions:\n"))
        game = Game(level.lev_1_easy, 'x', 'p', 'e')
        game.create_game()
        env = LabyrinthEnv(max_actions, game=game, map_h=10, map_w=10)

    elif wall_input == "2":
        max_actions = int(input("\tMax actions:\n"))
        game = Game(level.lev_1_medium, 'x', 'p', 'e')
        game.create_game()
        env = LabyrinthEnv(max_actions, game=game, map_h=10, map_w=10)

    elif wall_input == "3":
        max_actions = int(input("\tMax actions:\n"))
        game = Game(level.lev_1_hard, 'x', 'p', 'e')
        game.create_game()
        env = LabyrinthEnv(max_actions, game=game, map_h=10, map_w=10)
    else:
        print("End\n")
        sys.exit()

    QL = QLearning(env)
    utils.clear_screen()

    env.render()
    menu_input = input(
        "(1)\tTraining\n"
        "(2)\tExecute automatically\n"
        "(3)\tExecute step-by-step\n"
        "(0)\tExit\n"
    )
    utils.clear_screen()

    if menu_input == "1":
        print("\tTraining\n")
        QL.training(epochs=20000, steps=200, alpha=0.1,
                    gamma=1.0, eps=1.0, plot=True)

    elif menu_input == "2":
        print("\tExecute\n")
        QL.execute(step_by_step=False)

    elif menu_input == "3":
        print("\tExecute\n")
        QL.execute(step_by_step=True)

    else:
        print("End\n")


def lev2_menu():
    wall_input = input(
        "Choose the percentage of the wall:\n"
        "(1)\tLow\n"
        "(2)\tMedium\n"
        "(3)\tHigh\n"
    )

    env = None

    if wall_input == "1":
        max_actions = int(input("\tMax actions:\n"))
        game = Game(level.lev_2_easy, 'x', 'p', 'e')
        game.create_game()
        env = LabyrinthEnv(max_actions, game=game, map_h=20, map_w=20)

    elif wall_input == "2":
        max_actions = int(input("\tMax actions:\n"))
        game = Game(level.lev_2_medium, 'x', 'p', 'e')
        game.create_game()
        env = LabyrinthEnv(max_actions, game=game, map_h=20, map_w=20)

    elif wall_input == "3":
        max_actions = int(input("\tMax actions:\n"))
        game = Game(level.lev_2_hard, 'x', 'p', 'e')
        game.create_game()
        env = LabyrinthEnv(max_actions, game=game, map_h=20, map_w=20)

    else:
        print("End\n")
        sys.exit()

    QL = QLearning(env)
    utils.clear_screen()

    env.render()
    menu_input = input(
        "(1)\tTraining\n"
        "(2)\tExecute automatically\n"
        "(3)\tExecute step-by-step\n"
        "(0)\tExit\n"
    )
    utils.clear_screen()

    if menu_input == "1":
        print("\tTraining\n")
        QL.training(epochs=20000, steps=200, alpha=0.1,
                    gamma=1.0, eps=1.0, plot=True)

    elif menu_input == "2":
        print("\tExecute\n")
        QL.execute(step_by_step=False)

    elif menu_input == "3":
        print("\tExecute\n")
        QL.execute(step_by_step=True)

    else:
        print("\tEnd\n")


def lev3_menu():
    wall_input = input(
        "Choose the percentage of the wall:\n"
        "(1)\tLow\n"
        "(2)\tMedium\n"
        "(3)\tHigh\n"
    )

    env = None

    if wall_input == "1":
        max_actions = int(input("\tMax actions: "))
        game = Game(level.lev_3_easy, 'x', 'p', 'e')
        game.create_game()
        env = LabyrinthEnv(max_actions, game=game, map_h=30, map_w=30)

    elif wall_input == "2":
        max_actions = int(input("\tMax actions: "))
        game = Game(level.lev_3_medium, 'x', 'p', 'e')
        game.create_game()
        env = LabyrinthEnv(max_actions, game=game, map_h=30, map_w=30)

    elif wall_input == "3":
        max_actions = int(input("\tMax actions: "))
        game = Game(level.lev_3_hard, 'x', 'p', 'e')
        game.create_game()
        env = LabyrinthEnv(max_actions, game=game, map_h=30, map_w=30)

    else:
        print("End\n")
        sys.exit()

    QL = QLearning(env)
    utils.clear_screen()

    env.render()
    menu_input = input(
        "(1)\tTraining\n"
        "(2)\tExecute automatically\n"
        "(3)\tExecute step-by-step\n"
        "(0)\tExit\n"
    )
    utils.clear_screen()

    if menu_input == "1":
        print("Training\n")
        QL.training(epochs=20000, steps=200, alpha=0.1,
                    gamma=1.0, eps=1.0, plot=True)

    elif menu_input == "2":
        print("Execute\n")
        QL.execute(step_by_step=False)

    elif menu_input == "3":
        print("Execute\n")
        QL.execute(step_by_step=True)

    else:
        print("End\n")
