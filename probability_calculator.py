# This entrypoint file to be used in development. Start by reading README.md
# import prob_calculator
# from unittest import main

# prob_calculator.random.seed(95)
# hat = prob_calculator.Hat(blue=4, red=2, green=6)
# probability = prob_calculator.experiment(
#     hat=hat,
#     expected_balls={"blue": 2,
#                     "red": 1},
#     num_balls_drawn=4,
#     num_experiments=3000)
# print("Probability:", probability)

# # Run unit tests automatically
# main(module='test_module', exit=False)
import copy
import random

class Hat:

  ##Here is the syntax I found to get a variable amount of inputs to be stored as a dictionary of keys and values.
  def __init__(self, **kwargs):
    #self.__dict__.update(kwargs) #this creates self.__dict__ dictionary. However, creating the self.contents variable gets added to this dictionary so this won't work.
    #print(self.__dict__)
    #print(kwargs)
    #print(type(kwargs)) #dictionary!! That simplifies things
    self.full_dict = kwargs
    #print(self.full_dict)
    self.contents = list()

    #print(kwargs['yellow'])
    for key in kwargs:
      #print(kwargs[key])
      if kwargs[key] > 0: #if there is at least 1 ball of that color
        #print(range(kwargs[key]))
        for numb in range(kwargs[key]) :
          self.contents.append(key) #add the key in once for each count of it in the dictionary
          #print(self.contents)
    # print(self.full_dict)
    # print(self.contents)

    #Now get a total number of balls in the hat:
    self.count_balls =  0
    for key in kwargs :
      self.count_balls = self.count_balls + kwargs[key]
      #print(self.count_balls)

  def draw(self, pulls):
    #print(pulls)
    #print(type(pulls))
    #print(range(pulls))
    if pulls > self.count_balls : #if you try to pull more balls than are available in the hat
      print('Not enough balls to pull that many')
    else: #if there are enough balls in the hat to be make the number of pulls inputted
      for pull in range(pulls) :
        random_digit = random.randint(0, self.count_balls -1) #to get a random number from with number of remaining balls. Need to subtract one because it is shifted down by 1 by starting at zero
        # print(random_digit)
        #print('The color of the ball pulled is', self.contents[random_digit]) #Pick randomly from self.contents. The self.full_dict may have an entry in there with a zero value that we want to avoid
        #print()
        #print('The old dictionary is', self.full_dict)
        #print('The dictionary item to be remove is', self.contents[random_digit])
        #print(self.full_dict[self.contents[random_digit]])
        #print(type(self.full_dict[self.contents[random_digit]]))
        self.full_dict[self.contents[random_digit]] = self.full_dict[self.contents[random_digit]] - 1
        #print('The new dictionary is', self.full_dict)
        #print()
        #print('The old contents are', self.contents)
        self.contents.remove(self.contents[random_digit])
        #print('The new contents are', self.contents)
        self.count_balls = self.count_balls - 1 #Be sure to lower the count of remaining balls by 1 at the end of each draw!!!

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  hat_start = copy.deepcopy(hat)#Keep a version of the hat that has all of the balls it started with so it can start fresh with all the balls it started with.
  hat_start.contents = copy.deepcopy(hat.contents) #Same for contents
  hat_start.full_dict = copy.deepcopy(hat.full_dict) #Same for dictionary
  Yes = 0 #Get a running count of how many times the expected_balls are pulled
  for experiment in range(num_experiments):
    # print()
    # print('hat_start right before the draw is', hat_start.full_dict)
    # print('hat right before the draw is', hat.full_dict)
    hat.draw(num_balls_drawn) #pull the balls required for each experiment
    # print()
    # print('hat_start right after the draw is', hat_start.full_dict)
    # print('hat right after the draw is', hat.full_dict)
    ball_expectation_met = 0 # set up a variable to count each ball color that has an expected number of times being pulled
    for key in expected_balls: #to iterate through the expected balls see if expected_balls were indeed pulled or not
      # print(type(expected_balls))
      expectation = expected_balls[key]
      #print('Expected number of ', key, 'is', expectation)
      # print(type(hat_start.full_dict))
      # print(type(hat.full_dict))
      # print(hat_start.full_dict[key])
      # print(hat.full_dict[key])
      pulled = hat_start.full_dict[key] - hat.full_dict[key] # the difference between the starting value and the value after the drawing is done is the number of balls of that color that were pulled
      # print(expectation)
      #print('Number of ', key, 'pulled is', pulled)
      if pulled >= expectation: #if the expected balls were indeed pulled for the color/type being iterated on
        ball_expectation_met = ball_expectation_met + 1
      #print('ball_expectation_met is ', ball_expectation_met)

    if ball_expectation_met == len(expected_balls.keys()) : #if all balls with an expected number of pulls were actually pulled their respective expected number of times
      Yes = Yes + 1

    hat = copy.deepcopy(hat_start) #set hat back to starting position to it is set for another experiment to start over
    hat.contents = copy.deepcopy(hat_start.contents) #same with contents
    hat.full_dict = copy.deepcopy(hat_start.full_dict) #same with dictionary
  # print(Yes)
  # print(type(Yes))
  # print(str(Yes))
  # print(type(str(Yes)))
  probability = str(Yes) + '/' + str(num_experiments)
  print(probability)
  return probability




hat1 = Hat(yellow=3, blue=7, green=5, red=1)
experiment(hat1, {"red":1, "yellow":3}, 12, 1000)
