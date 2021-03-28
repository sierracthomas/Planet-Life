import random
import time

## Setting info
# Generate list that will determine setting.
name = str(input("What is your name? "))
setting_list = []
for i in range(0,5):
  setting_list.append(random.randint(0,2))

# Life list info
# Generate list that will determine life factors.
# Slot 0 is compass,
life_list = []
for i in range(0,4):
  life_list.append(random.randint(0,2))

# Determine if planet is capable of life
life_factors = 0
for i in life_list:
  life_factors += i

if life_factors > 5:
  life_factors = True
else:
  life_factors = False

## Dictionary for descriptors of the planet
descriptor_dict = {0: "green, with light blue clouds. ", 1: "red, with a slight breeze. ", 2: "very cold. "}

## Dictionaries for actions
# Dictionary for compass reading
compass_dict = {0: "Your compass does not change as you spin it. ", 1: "Your compass is broken, unfortunately. ", 2: "Your compass points north. "}
# Dictionary for energy source
energy_dict = {0: "The sky is dark. ", 1: "There are two bright suns. ", 2: "There is a sun out in the distance. "}
# Dictionary for temperature
temp_dict = {0: "10c. ", 1: "300c. ", 2: "2c. "}

# Make log list so that users can check observations
log = []

# Define function to print log whenever
def print_log():
  print("Loading observation log")
  time.sleep(.5)
  print("...")
  time.sleep(.5)
  for i in log:
    print(i)
  time.sleep(.5)

# Now we need functions for actions
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
  
# Floor stability can only be checked at cliff, so this will be inside cliff loop
def check_floor_stability():
  print("Checking floor stability. ")

# All possible actions to make `main()` smaller
# Need to make a nested loop so that each current location
# will determine what actions can be taken there
current_loc = "starting position"

# Now we need functions gameplay in locations                                                                                               
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

def possible_actions():
  action = "in progress"
  while not action.lower == "done":
    if current_loc == "cliff":
      action = input("Would you like to do anything here? ")
      if action.lower() == "compass":
        check_compass()
      if action.lower() == "temperature":
        check_temperature()
      if action.lower() == "energy":
        check_energy_source()
      if action.lower() == "floor":
        check_floor_stability()
      if action.lower() == "log":
        print_log()
      if action.lower() == "no":
        break
    if current_loc == "crater":
      action = input("Would you like to do anything here? ")
      if action.lower() == "compass":
        check_compass()
      if action.lower() == "temperature":
        print("Wow, it's exceptionally cold here. ")
      if action.lower() == "energy":
        check_energy_source()
      if action.lower() == "floor":
        print("The floor is compacted... (try this at the cliff!) ")
      if action.lower() == "log":
        print_log()
      if action.lower() == "no":
        break

# Introduce player to their new setting

def introduction():
  print("Welcome to your new planet,", name,". Your ship has crash-landed and left you stranded.")
  print("You are carrying food, a thermometer, a compass, an oxygen tank, and a good book.")
  print("To see what you have in your toolbelt, please type `help` at any time.")
  time.sleep(.5)
  print("You'll be here for a while.")
  print("\n \nYou look around. The planet is", descriptor_dict[setting_list[0]])
  print("To your left-hand side there is a large hill. \nTo your right-hand side there is a cliff. In front of you there is a deep crater. ")

# Enter while loop. Once broken, game ends.
# will take user inputs for location. after location, can do actions. 
# can do temp anywhere, can do compass anywhere. 
# can only do energy on hill. can only do floor stability on cliff. 
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
      print("You are carrying food, a thermometer, a compass, an oxygen tank, and a good book. ")
    if user_input.lower() == "log":
      print_log()
    if user_input.lower() == "done":
      break

introduction()
main()

# Ask user if planet can host life
user_input = input("\nThink this planet is capable of hosting life? ")
if user_input.lower() == "no":
  user_condition = False
if user_input.lower() == "yes":
  user_condition = True

if user_condition == life_factors:
  print("\nCongrats! That is correct! ")
else: 
  print("So sorry, try again! ")

