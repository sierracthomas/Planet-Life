import random
import time

## Setting info
# Generate list that will determine setting.
name = str(input("What is your name? "))
setting_list = []

# Life list info
# Generate list that will determine life factors.
life_list = []
life_factors = 0

def random_lists():
  for i in range(0,5):
    life_list.append(random.randint(0,2))
  for i in range(0,5):
    setting_list.append(random.randint(0,2))      

## Dictionary for descriptors of the planet
descriptor_dict = {0: "green, with light blue clouds. ", 1: "red, with a slight breeze. ", 2: "very sandy, with slight hills off in the distance and blue sky. "}

## Dictionaries for actions
# Dictionary for compass reading
compass_dict = {0: "Your compass aims wherever you point it. ", 1: "Your compass is broken, unfortunately. ", 2: "Your compass points north. "}
# Dictionary for energy source
energy_dict = {0: "The sky is dark. ", 1: "There are two bright suns. ", 2: "There is a sun out in the distance. "}
# Dictionary for temperature
temp_dict = {0: "0c. ", 1: "35c. ", 2: "20c. "}
# Dictionary for floor features
floor_dict = {0: "The floor feels solid.", 1: "The floor feels hollow. ", 2: "There's a weird vibration when you check. Is it underground water? "}
# Dictionary for soil pH
ph_dict = {0: "The pH strip turns a dark green, which you know to be a pH of around 10. ", 1: "The pH strip turns orangey-pink, which you know to be a pH of around 2. ", 2: "The pH strip turns yellow-green, which you know to be a pH of 5-6. "}

## Make log list so that users can check observations
log = []
# Define function to print log whenever
def print_log():
  print("Loading ", name ,"'s observation log")
  time.sleep(.5)
  print("...")
  time.sleep(.5)
  for i in log:
    print(i)
  time.sleep(.5)

## Now we need functions for actions
def check_compass():
  print("Checking compass. ")
  time.sleep(.5)
  print(compass_dict[life_list[0]])
  log.append(compass_dict[life_list[0]])

def check_energy_source():
  print("Checking energy source. ")
  time.sleep(.5)
  print(energy_dict[life_list[1]])
  log.append(energy_dict[life_list[1]])

def check_temperature():
  print("Checking temperature. ")
  time.sleep(.5)
  print(temp_dict[life_list[2]])
  log.append(temp_dict[life_list[2]])
  
def check_floor_stability():
  print("Checking the ground. ")
  time.sleep(.5)
  print(floor_dict[life_list[3]])
  log.append(floor_dict[life_list[3]])

def check_ph_soil():
  print("Using the pH test strip to check pH of soil. ")
  time.sleep(.5)
  print(ph_dict[life_list[4]])
  log.append(ph_dict[life_list[4]])

# Now we need functions to keep track of user's location
current_loc = "starting position"

def cliff():
  global current_loc
  current_loc = "cliff"
  print("Standing at the cliff. ")

def crater():
  global current_loc
  current_loc = "crater"
  print("Standing at the crater. ")

def mountain():
  global current_loc
  current_loc = "mountain"
  print("Standing at the mountain. ")

def action_help():
  print("If you would like to perform an action, type `compass`, `temperature`, `energy`, `floor`, `pH`, or `log`. ")
  print("If not, type `no`. ")

# mega function that has action options for each location (don't look too closely at how it was done...)
def possible_actions():
  action = "in progress"
  while not action.lower == "done":
    if current_loc == "cliff":
      action = input("Would you like to do anything here? ")
      if action.lower() == "help":
        action_help()
      if action.lower() == "compass":
        check_compass()
      if action.lower() == "temperature":
        check_temperature()
      if action.lower() == "energy":
        check_energy_source()
      if action.lower() == "floor":
        check_floor_stability()
      if action.lower() == "ph":
        check_ph_soil()
      if action.lower() == "log":
        print_log()
      if action.lower() == "no":
        break
    if current_loc == "crater":
      action = input("Would you like to do anything here? ")
      if action.lower() == "help":
        action_help()
      if action.lower() == "compass":
        check_compass()
      if action.lower() == "temperature":
        print("Wow, it's exceptionally cold here. ")
      if action.lower() == "energy":
        print("You can't locate one, but there may be an energy source. Is it blocked by the mountain? ")
      if action.lower() == "floor":
        print("The floor is compacted... (try this at the cliff!) ")
      if action.lower() == "ph":
        print("The floor is too compacted to sample. ")
      if action.lower() == "log":
        print_log()
      if action.lower() == "no":
        break
    if current_loc == "mountain":
      action = input("Would you like to do anything here? ")
      if action.lower() == "help":
        action_help()
      if action.lower() == "compass":
        check_compass()
      if action.lower() == "temperature":
        check_temperature()
      if action.lower() == "energy":
        check_energy_source()
      if action.lower() == "floor":
        check_floor_stability()
      if action.lower() == "ph":
        check_ph_soil()
      if action.lower() == "log":
        print_log()
      if action.lower() == "no":
        break

## Game starts - Introduce player to their new setting
def introduction():
  print("\nWelcome to your new planet,", name,". Your ship has crash-landed and left you stranded.")
  print("You are carrying food, a thermometer, a compass, an oxygen tank, and a good book.")
  print("You need to decide if this planet is capable of hosting life. ")
  print("If you are not sure what to do, please type `help` at any time.")
  time.sleep(.5)
  print("You'll be here for a while.")
  time.sleep(.5)
  print("\n \nYou look around. The planet is", descriptor_dict[setting_list[0]])
  print("To your left-hand side there is a large mountain. \nTo your right-hand side there is a cliff. In front of you there is a deep crater. ")
  time.sleep(.5)

# Body of game - explore planet
def main():
  user_input = "running"
  while not user_input.lower == "done":
    user_input = input("\nWhere would you like to go? ")
    if user_input.lower() == "cliff":
      cliff()
      possible_actions()
    if user_input.lower() == "crater":
      crater()
      possible_actions()
    if user_input.lower() == "mountain":
      mountain()
      possible_actions()
    if user_input.lower() == "help":
      print("If you would like to visit a location, type `mountain`, `cliff`, or `crater`. ")
      print("To view your observation log, type `log`. If you are ready, type `done`. ")
    if user_input.lower() == "log":
      print_log()
    if user_input.lower() == "done":
      break

# End of game - ask user if planet can host life
def life_question():
  user_input = input("\nThink this planet is capable of hosting life? ")
  if user_input.lower() == "no":
    user_condition = False
  if user_input.lower() == "yes":
    user_condition = True
  if user_condition == life_factors:
    print("\nCongrats! That is correct! ")
  else: 
    print("That was not correct, try again! ")

# Check if planet is Tatooine
def check_tatooine():
  if setting_list[0] == 2:
    if life_list[1] == 1:
      if life_list[2] == 1:
        print("Wait a second... This planet looks just like Tatooine! \nOff in the distance, you see a sprawling village of cave homes.")
        time.sleep(.5)
        print("Whew! You walk towards the village - hopefully someone there can help get you back to your planet. ")
        life_factors = 6

## Main program starts here - continue until user wants to stop
while True:
  # Generate randomness starting with empty lists
  life_list = []
  setting_list = []
  random_lists()
  # Determine if planet is capable of life
  for i in life_list:
    life_factors += i

  if life_factors > 5:
    life_factors = True
  else:
    life_factors = False
    
  # Body of game 
  introduction()
  main()
  check_tatooine()
  life_question()
  time.sleep(.5)
  if input("Would you like to play again? ").lower() != 'yes':
    print("Thanks for playing! ")
    break

