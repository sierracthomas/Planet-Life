[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1q2dF2F4y52boVLcHJhljLbg6ywJRssww?usp=sharing)

# Planet-Life
A fun game where the player determines if a planet is capable of hosting life. 

Instructions will go here

please see my repo on github for sources
 - Structure of game:
  - people will get a description of landing on a planet. the planet will be described with *setting*. 
  - let's have three main areas. A mountain (*maybe vegetation or anything else*), a crater (*with or without water or chemicals*), and a cliff. 
  - player can walk to any of the three locations and "inspect". A randomized location will have a special tool to inspect the terrain. Each one can come with a preset (*or one or two tools*). 
  - player can use compass to determine magnetic field
  - player can see stars/energy source on top of mountain 
  - player can take temperature of planet
  - player may experience earthquakes standing by the cliff. this used to be ocean dropoff, so may be fossils. or salt. 
  - Occasionally, the player is not equipped with the right outfit and tools and dies immediately haha. this will happen if no atmosphere. let's make this very unlikely
  - game asks, is life likely? y or n then you win or lose
  - github will have sources cited, instructions, and my notes

- structure of program
  - append randomness to list, then check to see if anything can support life. this can determine answers/let people go back, start with an empty list
  - add random numbers to each slot on list. from 0-3
  - each slot on list will be used as argument to input
  - list does not change so we can go back. if player says "cliff", call the "cliff" function with the correct argument. 
  - when player says "guess", then the game will ask if there is life. if every element in list adds up to some number, likely life. 
  - can we print out the reasons there are life? Maybe? substitute elements of list with the things we know to be true. maybe we need a dictionary to pair them  - we do. Compare elements of list to dictionary (or another list) and 10/10, then print 

