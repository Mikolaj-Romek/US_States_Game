import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
data = pandas.read_csv("50_states.csv")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
counter = 0
states = data.state.to_list()

lista = []
run = True
lack_of_knowledge = []


while run:
    answer_state = screen.textinput(title=f"{counter}/50 Guessed", prompt="What's another state's name?").title()
    if answer_state in states not in lista:
        state_data = data[data.state == answer_state]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(answer_state)
        lista.append(answer_state)
        counter += 1
    if answer_state == "Exit":
        statueta = [state for state in states if state not in lista]
        datale = pandas.DataFrame(statueta)
        datale.to_csv("states_to_learn.csv")
        run = False
    if counter == 50:
        run = False


screen.exitonclick()

df = pandas.DataFrame(lack_of_knowledge)
df.to_csv("learn_these.csv")

