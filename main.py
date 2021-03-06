import random
import time

## Setting info
# Generate list that will determine setting.
name = str(input("What is your name? "))
setting_list = []
for i in range(0,5):
  setting_list.append(random.randint(0,3))

# Dictionary for descriptors of the planet
descriptor_dict = {0: "green, with light blue clouds. ", 1: "red, with a slight breeze. ", 2: "very cold. "}

## Dictionaries for actions
# Dictionary for compass reading
compass_dict = {0: "Your compass points north. ", 1: "Your compass does not change as you spin it. ", 2: "Your compass is broken, unfortunately. "}
# Dictionary for energy source
energy_dict = {0: "The sky is dark. ", 1: "There are two bright suns. ", 2: "There is a sun out in the distance. "}
# Dictionary for temperature
temp_dict = {0: "10c. ", 1: "300c. ", 2: "2c. "}

# Life list info
# Generate list that will determine life factors.
# Slot 0 is compass, 
life_list = []
for i in range(0,4):
  life_list.append(random.randint(0,3))

# Now we need functions for actions
  def check_compass():
    print("Checking compass. ")
    time.sleep(.5)
    print(compass_dict[life_list[0]])
  
  def check_energy_source():
    print("Checking energy source. ")
    time.sleep(.5)
    print(energy_dict[life_list[1]])

  def check_temperature():
    print("Checking temperature. ")
    time.sleep(.5)
    print(temp_dict[life_list[2]])
  
# Floor stability can only be checked at cliff, so this will be inside cliff loop
  def check_floor_stability():
    print("Checking floor stability. ")

# Now we need functions for locations
  def cliff():
    print("Standing at the cliff. ")

  def crater():
    print("Standing at the crater. ")

  def mountain():
    print("Standing at the mountain. ")

# Introduce player to their new setting
print("Welcome to your new planet,", name,". Your ship has crash-landed and left you stranded.")
print("You are carrying food, a thermometer, a compass, an oxygen tank, and a good book.")
print("To see what you have in your toolbelt, please type `help` at any time.")
time.sleep(.5)
print("You'll be here for a while.")
print("\n \nYou look around. The planet is", descriptor_dict[setting_list[0]],"To your left-hand side there is a large hill. \nTo your right-hand side there is a cliff. In front of you there is a deep crater. ")

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
      action = input("Would you like to do anything here? ")
      if action.lower() == "yes":
        print("cool")
    if user_input.lower() == "crater":
      crater()
    if user_input.lower() == "mountain":
      mountain()
    if user_input.lower() == "help":
      print("You are carrying food, a thermometer, a compass, an oxygen tank, and a good book. ")
    if user_input.lower() == "done":
      break

main()
#  else: 
#    print("That's not an answer, silly! ")
#    time.sleep(5)
#    print("...")



