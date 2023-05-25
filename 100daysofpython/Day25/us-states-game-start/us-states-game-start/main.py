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

# Turtle.onscreenclick(get_mouse_click_error)
# Turtle.mainloop()

counter = int(0)
correct_guesses = []

# answer_state = screen.textinput(title="Guess Another State Name", prompt="What is the name of another state?")

df = pd.read_csv("50_states.csv")


while counter < 50:
    answer_state = screen.textinput(title=f"{counter}/50 guessed", prompt="What is the name of another state?")    
    guess = answer_state.title()
    guess_row = df[(df['state'] == guess)]
    x = int(guess_row.x)
    y = int(guess_row.y)
    if guess_row.empty == True:
        print('Not found')
    else:
        counter += 1
        correct_guesses.append(guess_row)
        print(guess_row, counter)

        # create new Turtle, Turtle go to 
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.color("black")
        state_turtle.goto((x,y))
        state_turtle.write(guess_row.state.item())
        state_turtle.st()
        
# if counter = 50, display you won message

    

print(guess_row)

screen.exitonclick()
