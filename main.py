import turtle
import pandas

IMAGE_PATH = "blank_states_img.gif"
STATES_PATH = "50_states.csv"
STATES_COUNT = 50
ALIGNMENT = "center"
STATE_FONT = ('Arial', 10, "bold")
FONT = ('Arial', 30, "bold")

correct_answers = []
correct_number = 0

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)
data = pandas.read_csv(STATES_PATH)
states = data.state.to_list()

game_on = True
label = turtle.Turtle()
label.penup()
label.hideturtle()

while game_on:
    answer = screen.textinput(title=f"Guess the State: {correct_number}/{STATES_COUNT}", prompt="Type a name of a state")
    answer = answer.capitalize()
    if answer in states and answer not in correct_answers:
        correct_answers.append(answer)
        correct_number += 1   
        state = data[data.state == answer]

        # Get x & y of the correctly guessed state
        x = int(state.x)
        y = int(state.y)

        label.goto(x, y)
        label.write(f"{answer}", True, align=ALIGNMENT, font=STATE_FONT)
    elif answer == "Exit":
        game_on = False
        screen.clear()
        label.goto(0, 0)
        label.write(f"You've completed {correct_number}/{STATES_COUNT}", True, align=ALIGNMENT, font=FONT)

        missing_states = []
        for state in states:
            if state not in correct_answers:
                missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
    if correct_number == STATES_COUNT:
        game_on = False
        label.goto(0, 0)
        label.write("COMPLETED - GREAT JOB!", True, align=ALIGNMENT, font=FONT)
screen.exitonclick()