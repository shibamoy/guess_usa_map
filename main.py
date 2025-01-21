import turtle
from turtle import Screen, Turtle
import pandas

pd = pandas.read_csv("50_states.csv")
state = (pd["state"])
x_point = pd["x"]
y_point = pd["y"]
print(pd[pd.state == "Ohio"]["x"])
state_dict = {state: (x_val, y_val) for state, x_val, y_val in zip(state, x_point, y_point)}
total = 50
current_states = 50 - len(state_dict)


screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def print_state(coor, state_name):
    writer = Turtle()
    writer.penup()
    writer.goto(coor)
    writer.pendown()
    writer.write(state_name)


while current_states != 50:
    total = 50
    current_states = 50 - len(state_dict)
    user_answer = screen.textinput(title= f"Guess the states{current_states}/{total}", prompt="What is the next state?").title()
    if user_answer in state_dict:
        state = user_answer
        coor = state_dict[user_answer]
        print_state(coor,state)
        state_dict.pop(user_answer)


turtle.mainloop()

