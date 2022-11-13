import turtle
import pandas

screen = turtle.Screen()
screen.setup(740, 500)
screen.title('U.S. States Game')
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
record_answer = []

while len(record_answer) < 50:
    answer = screen.textinput(f'{len(record_answer)} / 50 States Correct', "What is another state's name ?").title()

    if answer == 'Exit':
        missing_states = [new_state for new_state in all_states if new_state not in record_answer]
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv('states_to_learn.csv')
        break

    if answer in all_states:
        record_answer.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

screen.exitonclick()
