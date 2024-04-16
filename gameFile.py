# Object Center Point and Distance Calculation Algorithm for YOLOv8
# Program created by [Nithilan Rengapragash]
#
# MIT License
#
# Copyright (c) [2024] [Nithilan Rengapragash]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random

# Define the dungeon maps for each level
dungeons = [
    [
        ["S", ".", ".", ".", ".", ".", "."],
        [".", "#", "#", "#", ".", "#", "."],
        [".", ".", ".", "#", ".", "#", "."],
        ["#", "#", ".", "#", ".", ".", "."],
        [".", ".", ".", "#", "#", "#", "."],
        [".", "#", "#", "#", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "E"]
    ],
    [
        ["S", "#", ".", ".", ".", "#", "."],
        [".", "#", "#", "#", ".", "#", "."],
        [".", ".", ".", "#", ".", ".", "."],
        ["#", "#", ".", "#", "#", ".", "."],
        [".", ".", ".", "#", "#", "#", "."],
        [".", "#", "#", "#", ".", ".", "."],
        [".", ".", ".", ".", ".", "#", "E"]
    ],
    [
        ["S", ".", "#", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "."],
        [".", ".", "#", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "."],
        [".", ".", "#", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "."],
        [".", ".", "#", ".", "#", ".", "E"]
    ],
    [
        ["S", ".", ".", "#", ".", ".", "."],
        ["#", ".", "#", "#", "#", ".", "#"],
        [".", ".", "#", ".", "#", ".", "."],
        [".", "#", "#", ".", "#", ".", "#"],
        [".", "#", ".", ".", "#", ".", "#"],
        [".", "#", "#", "#", "#", ".", "#"],
        [".", ".", ".", ".", ".", ".", "E"]
    ]
]

# Player's starting position
player_pos = [0, 0]

# Current level
current_level = 0

# Define the game functions
def print_map():
    for row in dungeons[current_level]:
        print(" ".join(row))

def move_player(direction):
    global player_pos
    x, y = player_pos

    if direction == "left":
        y -= 1
    elif direction == "right":
        y += 1
    elif direction == "up":
        x -= 1
    elif direction == "down":
        x += 1

    if 0 <= x < len(dungeons[current_level]) and 0 <= y < len(dungeons[current_level][0]):
        if dungeons[current_level][x][y] != "#":
            player_pos = [x, y]
            return True
        else:
            print("Ouch! You hit a wall.")
    else:
        print("You cannot move outside the dungeon.")

    return False

# Game loop
while True:
    print("Level:", current_level + 1)
    print_map()

    direction = input("Which direction do you want to move? (up/down/left/right): ").lower()

    if direction in ["up", "down", "left", "right"]:
        if move_player(direction):
            if dungeons[current_level][player_pos[0]][player_pos[1]] == "E":
                print("Congratulations! You found the exit and proceed to the next level!")
                current_level += 1
                if current_level == len(dungeons):
                    print("You have completed all levels! Congratulations!")
                    break
                else:
                    player_pos = [0, 0]
                    print("Entering level", current_level + 1)
            elif dungeons[current_level][player_pos[0]][player_pos[1]] == ".":
                dungeons[current_level][player_pos[0]][player_pos[1]] = " "
    else:
        print("Invalid direction! Please enter up, down, left, or right.")
