import turtle, random, time

#reminder of bug 1: the turtle doesn't stop itself when it goes out of the screen

#create lists that represent different characteristics of the turtle
colors = ["red", "purple", "blue","orange", "green", "black", "pink"]
speed = [0,2,4,6,8,10]
width = [0.5,2,10,20,40]
turtle_list = []

#use random function to assign the turtle with random items from different lists
current_turtle = turtle.Turtle()
current_turtle.shape("turtle")
current_turtle.speed(random.choice(speed))
current_turtle.color(random.choice(colors))
current_turtle.width(random.choice(width))

#use penup function to get rid of the trace of the turtle's travel
current_turtle.penup()

turtle_list.append(current_turtle)

#these functions below make the turtle move in different directions    
def up():
    current_turtle.setheading(90)
    current_turtle.forward(100)
def down():
    current_turtle.setheading(270)
    current_turtle.forward(100)
def left():
    current_turtle.setheading(180)
    current_turtle.forward(100)
def right():
    current_turtle.setheading(0)
    current_turtle.forward(100)

#the function below indicates what will happen respectively when player 2 clicks on the turtle and misclicks
def clickleft(x,y):
    #make current_turtle a global variable so it can be used inside of the function
    global current_turtle

    #use for loop to check the distance between the x, y position of the mouse click and the x,y position of the turtle
    for hitted_turtle in turtle_list:
      x_distance = abs(hitted_turtle.xcor() - x)
      y_distance = abs(hitted_turtle.ycor() - y)
      if (x_distance < 10 and y_distance < 10):
        turtle_list.remove(hitted_turtle)
        hitted_turtle.ht()
    #reminder of bug 2:can't find a way to completely delete the turtle object, so the turtle clicked is only invisible on screen but still there
    if ((x_distance >= 10 or y_distance >= 10) and len(turtle_list) < 10):
           new_turtle = turtle.Turtle()
           new_turtle.shape("turtle")
           new_turtle.speed(random.choice(speed))
           new_turtle.color(random.choice(colors))
           new_turtle.width(random.choice(width))
           new_turtle.penup()
           turtle_list.append(new_turtle)

    #use if statements to indicate the two possible results of the game
    if len(turtle_list) == 10:
        #hide all the turtles to clear the screen
       for every_turtle in turtle_list:
           every_turtle.ht()          
       turtle.shape("turtle")
       turtle.write("Game over!", False, align = "center", font=("Arial", 20, "normal"))
       time.sleep(1)
       turtle.clear()
       turtle.write("Unity is strength. Player 1 won!", False, align = "center", font=("Arial", 20, "normal"))
       time.sleep(1)
    if len(turtle_list) == 0:
       turtle.shape("turtle")
       turtle.write("Game over!", False, align = "center", font=("Arial", 20, "normal"))
       time.sleep(1)
       turtle.clear()
       turtle.write("The Cheeky family perished. Player 2 won!", False, align = "center", font=("Arial", 20, "normal"))
       time.sleep(1)

#the funtion below switches control from the current turtle to any turtles in turtle_list
#reminder of bug 3: sometimes the control is switched to the same turtle
def switch():
    global current_turtle
    if len(turtle_list) > 1:
       current_turtle = random.choice(turtle_list)
  
#use the listen function to assign the functions above to their corresponding keys/click
turtle.listen()

turtle.onscreenclick(clickleft, 1)
turtle.onkey(up,'w')
turtle.onkey(down,'s')
turtle.onkey(left,'a')
turtle.onkey(right,'d')
turtle.onkey(switch, "space")

