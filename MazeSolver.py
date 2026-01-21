import os
import time
from stack import *

class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"
    
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
    
    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")

    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
                return True
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
                return True
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
                return True
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
                return True
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        

class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

# ------------------------ #
# ===== MAIN PROGRAM ===== #
# ------------------------ #

m = maze()
m.print()

stack = Stack()
stack.push(pos(0,0))

def reverse():
    reverseStack = Stack()
    while True:
        if m.ply.y-1 == stack.peek().y:
            reverseStack.push(m.ply)
            stack.pop()
            m.move_up()
        elif m.ply.y+1 == stack.peek().y:
            reverseStack.push(m.ply)
            stack.pop()
            m.move_down()
        elif m.ply.x-1 == stack.peek().x:
            reverseStack.push(m.ply)
            stack.pop()
            m.move_left()
        elif m.ply.x+1 == stack.peek().x:
            reverseStack.push(m.ply)
            stack.pop()
            m.move_right()

        m.print()

        if m.ply.y-1 != stack.peek().y and m.ply.y-1 != reverseStack.peek().y and m.maze[m.ply.y-1][m.ply.x] != "X":
            stack.push(m.ply)
            m.move_up()
            return
        elif m.ply.y+1 != stack.peek().y and m.ply.y+1 != reverseStack.peek().y and m.maze[m.ply.y+1][m.ply.x] != "X":
            stack.push(m.ply)
            m.move_down()
            return
        elif m.ply.x-1 != stack.peek().x and m.ply.x-1 != reverseStack.peek().x and m.maze[m.ply.y][m.ply.x-1] != "X":
            stack.push(m.ply)
            m.move_left()
            return
        elif m.ply.x+1 != stack.peek().x and m.ply.x+1 != reverseStack.peek().x and m.maze[m.ply.y][m.ply.x+1] != "X":
            stack.push(m.ply)
            m.move_right()
            return

while True:
    m.print()
    prev_grid = m.ply
    if m.ply.y-1 != stack.peek().y:
        if m.move_up():
            stack.push(prev_grid)
            continue
    if m.ply.y+1 != stack.peek().y:
        if m.move_down():
            stack.push(prev_grid)
            continue
    if m.ply.x-1 != stack.peek().x:
        if m.move_left():
            stack.push(prev_grid)
            continue
    if m.ply.x+1 != stack.peek().x:
        if m.move_right():
            stack.push(prev_grid)
            continue
    if m.move_up() == False or m.move_down() == False or m.move_left() == False or m.move_right() == False:
        m.printEND()
        break
    reverse()