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

#Store the pear file name in case it needs to be used as a fruit shape instead of the apple
pear_image = "pear.gif"

#Create a display for the game and define its properties
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

#Add a background layer using the provided image and add an apple to it
wn.bgpic("background.gif")
wn.addshape(apple_image)


#####-Game Config-#####
#Set how many apples you want to display on screen
num_apples = 5

#Set a falling speed of the apples
falling_speed = 8

#Define each of the letters of the aplphapbet in a list of letters to be taken from for apples
available_letters_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#Create lists to track each apple and their corresponding letters
apple_list = []
apple_letter_list = []

#For loop to generate 5 apples on a tree at the same time and track them using lists
for i in range(num_apples):
  #Create an apple as a turtle and add it to the apple list for tracking
  individual_apple = trtl.Turtle()
  apple_list.append(individual_apple)

  #Generate a random letter to draw on the apple and removed the used letter from the available list
  global drawn_letter #Allow the drawn letter variable to be accessed elsewhere in the code
  drawn_letter = available_letters_list[rand.randint(0,len(available_letters_list)-1)] #Grab random letter from random letters list

  #Add the apple's letter to the apple letter list to track it with its corresponding apple
  apple_letter_list.append(drawn_letter) 


#####-Functions-######
#Define a function to draw an apple with the parameter of the index of the apple being acted on, controlled by the main for loop
def draw_apple(index):
  #Draw the background of the apple based on the given image
  apple_list[index].shape(apple_image)

  #Draw the letter on the apple
  apple_list[index].penup() #Eliminate tracer
  apple_list[index].color("white") #Set the color to white

  #Dont trace to prevent unwanted movement and appear instantaneous
  wn.tracer(False)

  #Write a centered letter and align it vertically
  apple_list[index].goto(apple_list[index].xcor(), apple_list[index].ycor() - 35)
  apple_list[index].write(apple_letter_list[index], align = "center", font = ("Arial", 40, "normal"))
  apple_list[index].goto(apple_list[index].xcor(), apple_list[index].ycor() + 35)

  #Turn the tracer back on and update the screen
  wn.tracer(True)
  wn.update()

#Define a function to move an apple from the tree to the ground when it is falling with the parameter of the index of the apple being acted on, controlled by the main for loop
def falling_apple(index):
  #Define initial attributes for movement
  global y_moving_distance #Allow this variable to be accessed in other functions
  y_moving_distance = 150
  apple_list[index].penup()
  apple_list[index].speed(falling_speed)

  #Remove the unwanted letter
  apple_list[index].clear()

  #Drop the apple
  apple_list[index].goto(apple_list[index].xcor(), apple_list[index].ycor() - y_moving_distance)

  #Remove the unwanted apple
  apple_list[index].hideturtle()

  #Send the apple to a new location
  new_location(index)

#Define a function to send the apple to a new location with the parameter of the index of the apple being acted on, controlled by the main for loop
def new_location(index):
  #Check if there are no more new letters in the alphabet to pick from
  if (len(available_letters_list) > 0):
    #Define random x and y positions within the tree that the apple can occupy
    y_tree_variation = rand.randint(0,150)
    x_tree_variation = rand.randint(-100,100)
    
    #Send the apple to the new random location in the tree
    apple_list[index].goto(x_tree_variation, y_tree_variation)

    #Grab random letter from random letters list to make the letter randomized 
    apple_letter_list[index] = available_letters_list[rand.randint(0,len(available_letters_list)-1)] 

    #Draw and show a fresh apple in the new location
    draw_apple(index)
    apple_list[index].showturtle()

  #Output error message in terminal if there are no more available letters
  else:
    print("there are no more possible letters in the list")

#Function defenition to drop the apple if a specifc key is pressed
def a_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "a":
      #Proceed with dropping the apple
      falling_apple(i)

def b_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "b":
      #Proceed with dropping the apple
      falling_apple(i)

def c_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "c":
      #Proceed with dropping the apple
      falling_apple(i)

def d_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "d":
      #Proceed with dropping the apple
      falling_apple(i)

def e_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "e":
      #Proceed with dropping the apple
      falling_apple(i)

def f_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "f":
      #Proceed with dropping the apple
      falling_apple(i)

def g_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "g":
      #Proceed with dropping the apple
      falling_apple(i)

def h_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "h":
      #Proceed with dropping the apple
      falling_apple(i)

def i_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "i":
      #Proceed with dropping the apple
      falling_apple(i)

def j_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "j":
      #Proceed with dropping the apple
      falling_apple(i)

def k_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "k":
      #Proceed with dropping the apple
      falling_apple(i)

def l_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "l":
      #Proceed with dropping the apple
      falling_apple(i)

def m_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "m":
      #Proceed with dropping the apple
      falling_apple(i)

def n_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "n":
      #Proceed with dropping the apple
      falling_apple(i)

def o_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "o":
      #Proceed with dropping the apple
      falling_apple(i)

def p_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "p":
      #Proceed with dropping the apple
      falling_apple(i)

def q_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "q":
      #Proceed with dropping the apple
      falling_apple(i)

def r_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "r":
      #Proceed with dropping the apple
      falling_apple(i)

def s_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "s":
      #Proceed with dropping the apple
      falling_apple(i)

def t_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "t":
      #Proceed with dropping the apple
      falling_apple(i)

def u_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "u":
      #Proceed with dropping the apple
      falling_apple(i)

def v_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "v":
      #Proceed with dropping the apple
      falling_apple(i)

def w_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "w":
      #Proceed with dropping the apple
      falling_apple(i)

def x_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "x":
      #Proceed with dropping the apple
      falling_apple(i)

def y_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "y":
      #Proceed with dropping the apple
      falling_apple(i)

def z_pressed():
  #For loop to run the checks and function calls for all 5 apples
  for i in range(num_apples):
    #Check if the letter has actually been pressed
    if apple_letter_list[i] == "z":
      #Proceed with dropping the apple
      falling_apple(i)


#####-Function Calls-######
#For loop to draw the correct number of apples on the screen
for i in range(num_apples):
  draw_apple(i) #Pass the index through other functions as a parameter to know which apple to draw

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