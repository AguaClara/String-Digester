#######################################################################
# Interactive Tutorial 2: Python Basics
#######################################################################
# Comments beginning with "TODO" contain the tasks that you must
# complete in this interactive tutorial. Write your answers under each
# TODO. Use Find (Ctrl/Cmd + F) to keep track of them.
#
# This is a Python file, not the interactive interpreter, so code won't
# run immediately when you write it. You also WON'T need the triple
# greater-than symbols (>>>) at the beginning of each line.
#
# Just focus on writing Python to the best of your abilities! Once
# you're done, you'll have the chance to check your work in the next
# tutorial section, Running Python Code: https://bit.ly/2w3PbCX
#######################################################################

#######################################################################
# Don't touch this! This is for testing your code.
#######################################################################
from tests.prints import start_recording, stop_recording, get_prints
from tests.tutorial2 import test_todos

start_recording()
#######################################################################

# TODO 1: Write Monroe's favorite food in a string.
#
# Hint: It's rice and beans. Yum, string beans.

favorite_food = 'rice and beans' # Your answer here

print(favorite_food)

# TODO 2: Calculate the volume of a 7 x 7 x 5 cube using Python math
# operations.

volume = (7 * 7 * 5) # Your answer here

print(volume)

# TODO 3: Pop the last item from this list, append 'filtration' to it,
# then change the second item to '1 LPS'. Don't change the original
# list.
#
# Hint: what number do Python lists start from? Check the lists section
# in the Writing Python Code tutorial if you're unsure.

hydraulic_processes = ['flocculation', 'sedimentation', 'stirring']

# Your answer here

hydraulic_processes.pop()
hydraulic_processes.append('filtration')
hydraulic_processes[1] = '1 LPS'


print(hydraulic_processes)

# TODO 4: Change the value of the second entry in this dict to 'bacon'.
# Don't change the original dict.

analogy = {'knowledge' : 'power', 'France': 'ham'}

# Your answer here

analog['France'] = 'bacon'

print(analogy['knowledge'] + ' ' + analogy['France'])

# TODO 5: Write a conditional statement that determines if both of
# the following conditions are met:
#       - Either a or b are True
#       - c is False
# If both conditions are met, set does_it_work to 'yes'. Otherwise,
# set it to 'no'.

# Don't try to figure these variables out! Just write a conditional
# that determines if the above conditions are met.
a = True and False or not False or False
b = True and not False or True and False
c = False or not False and True or True

does_it_work = 'maybe'

# Your answer here


if(a == True or b == True and c == False):
    does_it_work = 'yes'

else:
    does_it_work = 'no'

print(does_it_work)

# TODO 6: Write a for loop that multiplies x by each integer from 1 to
# 30.
#
# Hint: what does += do? Check the for loops section in the Writing
# Python Code tutorial if you're unsure. Try it with multiplication.

x = 1

# Your answer here

for i in range(1, 31):
    x = x * i

print(x)

# TODO 7: Write a function called 'squared' that takes in a number and
# returns its square (to the power of 2). Then, call that function so
# that x is squared 6 times.
#
# Hint: Don't copy and paste the function 6 times!

x = 4

# Your answer here
def squared(y):
    y = y ** 2

for i in range(6):
    squared(x)

print(x)

#######################################################################
# Don't touch this! This is for testing your code.
#######################################################################
stop_recording()
test_todos(get_prints())
#######################################################################
