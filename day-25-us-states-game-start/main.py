import turtle
import pandas
from game_turtle import Game_Turtle

data = pandas.read_csv("50_states.csv")
missing_states = data["state"].tolist()

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

game_is_on = True
show_text_input = True
correct_states = []

game_turtle = Game_Turtle()

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        for state in correct_states:
            missing_states.remove(state)

        new_data = pandas.DataFrame(missing_states, columns=["State"])
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data.state.values and answer_state not in correct_states:
        correct_states.append(answer_state)
        answer_data = data[data.state == answer_state].values.flatten().tolist()
        game_turtle.display_state(answer_data)

# states_to_learn.csv


