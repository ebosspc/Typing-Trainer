'''
PLTW Lesson 1.2.3
@authors: Ethan Francolla, Ibrahim Haroon
'''
#Import turtle library for drawing functions and display
import turtle as trtl

#Import random library to generate random values to be used later
import random as rand

#####-Setup-#####
#Store the apple file name
apple_image = "apple.gif"

#Store the pear file name
pear_image = "pear.gif"

#Create a display for the game and define its properties
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

#Add a background layer using the provided image and add an apple to it
wn.bgpic("background.gif")
wn.addshape(apple_image)

#Define the apple as a turtle object
apple = trtl.Turtle()


#####-Game Config-#####
#Define each of the letters of the aplphapbet in a list of letters to be taken from for apples
letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


#####-Functions-######
#Define a function to draw an apple
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update() #Update the screen

#Define a function to move an apple from the tree to the ground when it is falling
def falling_apple():
  #Define initial attributes for movement
  global y_moving_distance #Allow this variable to be accessed in other functions
  y_moving_distance = 150
  apple.penup()
  apple.speed(3)

  #Remove the unwanted letter
  remove_letter(apple)

  #Drop the apple
  apple.goto(apple.xcor(), apple.ycor() - y_moving_distance)

  #Remove the unwanted apple
  remove_apple(apple)

  #Send the apple to a new location
  new_location(apple)

  
#Draw the letter on the apple
def draw_letter(active_apple):
  #Set initial attributes
  active_apple.penup() #Eliminate tracer
  active_apple.color("white")

  #Dont trace to prevent unwanted movement and appear instantaneous
  wn.tracer(False)

  #Grab a random letter from the alphabet to draw on the apple
  grab_letter()

  #Write a centered letter and align it vertically
  active_apple.goto(active_apple.xcor(), active_apple.ycor() - 35)
  active_apple.write(drawn_letter, align = "center", font = ("Arial", 40, "normal"))
  active_apple.goto(active_apple.xcor(), active_apple.ycor() + 35)

  #Turn the tracer back on
  wn.tracer(True)

  #Update screen to show untraced lines
  wn.update()

#Define a function to remove unwanted letters after the user has made them fall
def remove_letter(active_apple):
  #Remove letter
  active_apple.clear()

#Define a function to remove unwanted apples after the user has made them fall
def remove_apple(active_apple):
  #Remove apple
  active_apple.hideturtle()

#Define a function to show apples after they have reached their new location
def show_apple(active_apple):
  #Show apple
  active_apple.showturtle()

#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters

def new_location(active_apple):
  #Check if there are no more new letters in the alphabet to pick from
  if (len(letter_list) > 0):
    #Define random x and y positions within the tree that the apple can occupy
    y_tree_variation = rand.randint(0,150)
    x_tree_variation = rand.randint(-100,100)
    
    #Send the apple to the new random location
    active_apple.goto(x_tree_variation, y_tree_variation)

    #Show the apple in its new location
    show_apple(apple)
    draw_letter(apple)

  else:
    print("there are no more possible letters in the list")


#Define a function to take a letter of the alphabet from the list, draw it on the apple, and never use that letter again
def grab_letter():
    #Define the letter to be drawn from the list at random
    global drawn_letter #Allow this variable to be accessed elsewhere in the program
    drawn_letter = letter_list[rand.randint(0,len(letter_list)-1)]

    #Remove the used letter from the list to update the list to only unused letters
    letter_list.remove(str(drawn_letter))

#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
#for i in range(0, number_of_apples):
  #Your code here

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#Function defenition if a specifc key is pressed
def a_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "a":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def b_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "b":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def c_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "c":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def d_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "d":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def e_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "e":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def f_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "f":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def g_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "g":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def h_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "h":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def i_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "i":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def j_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "j":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def k_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "k":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def l_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "l":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def m_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "m":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def n_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "n":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def o_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "o":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def p_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "p":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def q_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "q":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def r_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "r":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def s_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "s":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def t_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "t":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def u_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "u":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def v_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "v":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def w_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "w":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def x_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "x":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def y_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "y":
    #Proceed with dropping the apple
    falling_apple()

#Function defenition if a specifc key is pressed
def z_pressed():
  #Check if the letter has actually been pressed
  if drawn_letter == "z":
    #Proceed with dropping the apple
    falling_apple()



#####-Function Calls-######
#Draw apple
draw_apple(apple)

#Draw Letter
draw_letter(apple)

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(a_pressed, "a")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(b_pressed, "b")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(c_pressed, "c")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(d_pressed, "d")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(e_pressed, "e")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(f_pressed, "f")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(g_pressed, "g")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(h_pressed, "h")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(i_pressed, "i")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(j_pressed, "j")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(k_pressed, "k")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(l_pressed, "l")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(m_pressed, "m")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(n_pressed, "n")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(o_pressed, "o")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(p_pressed, "p")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(q_pressed, "q")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(r_pressed, "r")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(s_pressed, "s")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(t_pressed, "t")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(u_pressed, "u")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(v_pressed, "v")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(w_pressed, "w")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(x_pressed, "x")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(y_pressed, "y")

#Drop the apple on the ground when the key specified below is pressed
wn.onkeypress(z_pressed, "z")

#Wait for user to press keys
wn.listen()

#Keep display running and persistent
wn.mainloop()


