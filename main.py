import turtle
import pandas

IMAGE_PATH = "blank_states_img.gif"
STATES_PATH = "50_states.csv"
STATES_COUNT = 50
ALIGNMENT = "center"
FONT = ('Arial', 10, "bold")

correct_answers = []
correct_number = 0

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)
data = pandas.read_csv(STATES_PATH)
states = data.state.to_list()

game_on = True

while game_on:
    answer = screen.textinput(title="Guess the State", prompt="Type a name of a state")
    answer = answer.capitalize()
    if answer in states and answer not in correct_answers:
        correct_answers.append(answer)
        correct_number += 1   
        state = data[data.state == answer]

        # Get x & y of the correctly guessed state
        x = state["x"].to_list()[0]
        y = state["y"].to_list()[0]

        label = turtle.Turtle()
        label.penup()
        label.hideturtle()
        label.goto(x, y)
        label.write(f"{answer}", True, align=ALIGNMENT, font=FONT)

screen.exitonclick()