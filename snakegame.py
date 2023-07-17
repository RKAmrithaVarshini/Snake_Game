from tkinter import *
import random

GAMEWIDTH=500
GAMEHEIGHT=500
SPEED=200
SPACESIZE=50
BODYPART=3
SNAKECOLOR="violet"
FOODCOLOUR="red"
BACKGROUND="black"

class Snake:
    
    def __init__(self):
        self.bodysize=BODYPART
        self.coordinates= []
        self.squares = []

        for i in range(0, BODYPART):
            self.coordinates.append([0,0])
        
        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x + SPACESIZE, y+SPACESIZE, fill=SNAKECOLOR,tag="snake")
            self.squares.append(square)


class Food:
    
    def __init__(self):

        x= random.randint(0,(GAMEWIDTH/SPACESIZE)-1)*SPACESIZE
        y= random.randint(0,(GAMEHEIGHT/SPACESIZE)-1)*SPACESIZE

        self.coordinates=[x, y]

        #creating the "food" for the snake
        canvas.create_oval(x,y,x+SPACESIZE,y+SPACESIZE,fill=FOODCOLOUR,tag="food")


def nextturn(snake, food):
    
    x,y = snake.coordinates[0]

    if direction=="up":
        y -= SPACESIZE
    elif direction=="down":
        y += SPACESIZE
    elif direction=="left":
        x -= SPACESIZE
    elif direction=="right":
        x += SPACESIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACESIZE, y + SPACESIZE, fill=SNAKECOLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score+=1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if checkcollision(snake):
        gameover();
    else:
        window.after(SPEED, nextturn, snake, food)


def directionchange(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    
    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def checkcollision(snake):
    x, y = snake.coordinates[0]

    if x<0 or x>= GAMEWIDTH:
        print("Game over")
        return True
    
    elif y<0 or y>= GAMEHEIGHT:
        print("Game over")
        return True
    
    for bodypart in snake.coordinates[1:]:
        if x == bodypart[0] and y == bodypart[1]:
            print("Game over")
            return True
        
    return False

def gameover():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('Comic Sans MS', 50), text ="GAME OVER", fill = "white", tag="gameover")
window = Tk()
window.title("snake game")
window.resizable(False,False)

score=0
direction='down'

label = Label(window, text="Score:{}".format(score), font=('consolas',40))
label.pack()

canvas= Canvas(window, bg=BACKGROUND, height=GAMEHEIGHT, width=GAMEWIDTH)
canvas.pack()

window.update()

windowwidth= window.winfo_width()
windowheight=window.winfo_height()
screenwidth=window.winfo_screenwidth()
screenheight=window.winfo_screenheight()

x =int((screenwidth/2) - (windowwidth/2))
y = int((screenheight/2) - (windowheight/2))

window.geometry(f"{windowwidth}x{windowheight}+{x}+{y}")

window.bind('<Left>', lambda event: directionchange('left'))
window.bind('<Right>', lambda event: directionchange('right'))
window.bind('<Up>', lambda event: directionchange('up'))
window.bind('<Down>', lambda event: directionchange('down'))

snake = Snake()
food = Food()

nextturn(snake, food)
window.mainloop()

