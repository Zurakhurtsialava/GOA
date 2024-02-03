from tkinter import *
import random

# RECORD = 55

GAME_WIDTH = 1000
GAME_HEIGHT = 1000
sPEED = 19
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = 'blue'
FOOD_COLOR = '#e61010'
BACKGROUND_COLOR = 'black'


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+ SPACE_SIZE, y+ SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH//SPACE_SIZE)-10) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT//SPACE_SIZE)-5) * SPACE_SIZE

        self.coordinates = [x, y]
        self.coordinates = [x, y]
        

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags='food')


def Next_Turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    # head of the snake
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score 
        score += 1
        # Update the score label
        canvas.delete('food')
        label.config(text="Score: {}".format(score))
        food = Food()
    else:
        # Remove the last element of the snake and its corresponding square
        canvas.delete(snake.squares[-1])
        snake.squares.pop()
        snake.coordinates.pop()

    # Check for collisions
    if Check_Colisssions(snake):
        GAME_OVER()
    else:
        window.after(sPEED - score, Next_Turn, snake, food)


def Change_Direction(New_Direction):
    
    global direction

    if New_Direction == 'left':
        if direction != 'right':
            direction = New_Direction
    elif New_Direction == 'right':
        if direction != 'left':
            direction = New_Direction
    elif New_Direction == 'up':
        if direction != 'down' :
            direction = New_Direction
    elif New_Direction == 'down':
        if direction != 'up':
            direction = New_Direction

def Check_Colisssions(snake):

    x, y = snake.coordinates[0]


    if x < 0 or x > GAME_WIDTH:
        print("GAME OVER")
        return True
    elif y < 0 or y > GAME_HEIGHT:
        print("GAME OVER")
        return True
    
    for square in snake.coordinates[1:]:
        if x == square[0] and y == square[1]:
            return True

    return False

def GAME_OVER():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 - 30, font=('consolas', 20), text="GAME OVER", tag='gameover')

def restart_game():
    canvas.delete(ALL)
    global score, direction
    score = 0
    direction = 'down'
    label.config(text="Score:{}".format(score))
    canvas.delete('snake', 'food')
    snake = Snake()
    food = Food()
    Next_Turn(snake, food)

window = Tk()
window.title("Hungry_Snake")

score = 0
direction = 'down'
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


window.bind('<Left>', lambda event: Change_Direction('left'))
window.bind('<Right>', lambda event: Change_Direction('right'))
window.bind('<Up>', lambda event: Change_Direction('up'))
window.bind('<Down>', lambda event: Change_Direction('down'))
window.bind('<a>', lambda event: Change_Direction('left'))
window.bind('<d>', lambda event: Change_Direction('right'))
window.bind('<w>', lambda event: Change_Direction('up'))
window.bind('<s>', lambda event: Change_Direction('down'))
window.bind('<r>', lambda event: restart_game())


snake = Snake()
food = Food()

Next_Turn(snake, food)

window.mainloop()