from tkinter import *

class PingPong():
     def __init__(self):
          pass
def move_ai_racket():
    x1, _, x2, _ = canvas.coords(ball)
    _, _, ai_x2, _ =canvas.coords(ai_racket_id)
    ai_racket_pos = canvas.coords(ai_racket_id)
    if ai_x2 < x1 and ai_racket_pos[2] < game_width:
        canvas.move(ai_racket_id, 2, 0)
    elif ai_x2 > x2 and ai_racket_pos[0] > 0 :
        canvas.move(ai_racket_id, -2, 0)
     
def change_direction(new_direction):
    global direction

    racket_pos = canvas.coords(racket_id)

    if new_direction == "left" and racket_pos[0] > 0:
        canvas.move(racket_id, -20, 0)

    elif new_direction == "right" and racket_pos[2] < game_width:
        canvas.move(racket_id, 20, 0)

def collision():
    global dx, dy
    x1, y1, x2, y2 = canvas.coords(ball)
    user_racket_pos = canvas.coords(racket_id)
    ai_racket_pos = canvas.coords(ai_racket_id)
    if y1 <= user_racket_pos[3] and x2 >= user_racket_pos[0] and x1 <= user_racket_pos[2]:
        dy = -dy
        

    if y2 >= ai_racket_pos[1] and x2 >= ai_racket_pos[0] and x1 <= ai_racket_pos[2]:
        dy = -dy

    # Check collision with walls
    if x1 <= 0 or x2 >= game_width :
        dx = -dx
    if y1 <= 0:
        dy = -dy
        canvas.coords(ball,game_height/2+5,game_width/2+5,game_height/2-5,game_width/2-5)
        increment()

        
def update_score():
    score = int(score_label.cget('text').split(' ')[-1])
    score_label.configure(text=f'Score: {score}')
    window.after(100, update_score)
def increment():
    score = int(score_label.cget('text').split(' ')[-1])
    score_label.configure(text=f'Score: {score + 1}')


def animation():
    global dx; global dy
    x1, y1, x2, y2 = canvas.coords(ball)
    if x2 > game_width or x1 < 0: 
        dx = - dx
    if y2 > game_height or y1 < 0:
        dy = - dy
    canvas.move(ball, dx, dy)
    collision()
    move_ai_racket()
    canvas.after(2, animation)

window = Tk()
game_width = 700
game_height = 700
racket_colour = "#000000"
racket_colour_ai = "#0000FF"
ball_colour = "#FF0000"
background = "#000000"
score = 0
direction = "left"
window.title("PingPong")
score_label = Label(window, text='Score: 0', font=('Arial', 16))
score_label.pack()
canvas = Canvas(window, bg="white", height=game_height, width=game_width)
ball = canvas.create_oval(100,100,125,125,fill="red")
canvas.coords(ball, game_width / 2 - 5, game_height / 2 - 5, game_width / 2 + 5, game_height / 2 + 5)
#Ball Speed Variables: (dx,dy)
dx = 0.5
dy = -0.5
ai_dx = 1
ai_dy = 0 
canvas.pack()
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Create the user racket
racket_id = canvas.create_rectangle(0, 0, 100, 10, fill=racket_colour)
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
canvas.move(racket_id, x, 10)

# Create the AI racket
ai_racket_id = canvas.create_rectangle(0, game_height - 10, 100, game_height, fill=racket_colour_ai)
canvas.move(ai_racket_id, game_width / 2 - 50, 0)

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))

animation()
window.mainloop()
