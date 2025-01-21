import turtle
from turtle import Screen
import pandas

pd = pandas.read_csv("50_states.csv")
state = (pd["state"])
x_point = pd["x"]
y_point = pd["y"]
print(pd[pd.state == "Ohio"])




screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

user_answer = screen.textinput(title= "Guess the states", prompt="What is the next state?").title()
print(user_answer)
turtle.mainloop()
