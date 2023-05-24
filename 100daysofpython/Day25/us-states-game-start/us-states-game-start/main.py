# US states game that allows users to guess the name of a state
# then puts them on the map using the coordinates in the csv


import turtle
import pandas as pd

screen = turtle.Screen()
screen.title = "US States Game"
img = "./blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


# def get_mouse_click_error(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_error)
# turtle.mainloop()

counter = 0

answer_state = screen.textinput(title="Guess Another State Name", prompt="What is the name of another state?")
print(answer_state)

guess = answer_state.title()
print(guess)
df = pd.read_csv("50_states.csv")
guess_row = df[(df['state'] == guess)]

if guess_row.empty == True:
    print('Not found')
else:
    print('Found, now we plot')
    counter += 1
    # create new turtle, turtle go to 
    xy = turtle.goto(guess_row.x, guess_row.y)

    

print(guess_row)

screen.exitonclick()
