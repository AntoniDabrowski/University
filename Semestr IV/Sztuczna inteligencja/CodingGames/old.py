import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


number_of_cells = int(input())  # 37
for i in range(number_of_cells):
    # index: 0 is the center cell, the next cells spiral outwards
    # richness: 0 if the cell is unusable, 1-3 for usable cells
    # neigh_0: the index of the neighbouring cell for each direction
    index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]

# game loop
while True:
    day = int(input())  # the game lasts 24 days: 0-23
    nutrients = int(input())  # the base score you gain from the next COMPLETE action
    # sun: your sun points
    # score: your current score
    sun, score = [int(i) for i in input().split()]
    inputs = input().split()
    opp_sun = int(inputs[0])  # opponent's sun points
    opp_score = int(inputs[1])  # opponent's score
    opp_is_waiting = inputs[2] != "0"  # whether your opponent is asleep until the next day
    number_of_trees = int(input())  # the current amount of trees

    my_trees = dict()
    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])  # location of this tree
        size = int(inputs[1])  # size of this tree: 0-3
        is_mine = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        if is_mine:
            if cell_index < 7:
                richness = 3
            elif cell_index < 19:
                richness = 2
            else:
                richness = 1
            my_trees[cell_index] = richness

    number_of_possible_moves = int(input())
    possible_moves = []
    for i in range(number_of_possible_moves):
        possible_move = input()
        possible_moves.append(possible_move)

    l = sorted(my_trees, key=my_trees.get, reverse=True)
    if len(possible_moves) > 1:
        print("COMPLETE " + str(l[0]))
    else:
        print(possible_moves[0])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>
    # print("WAIT")
