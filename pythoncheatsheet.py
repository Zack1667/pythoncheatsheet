# Variables and strings 

# hello world
print("Hello World!")

# hello world with a variable 

msg = "Hello World!"
print(msg)

# Concatenation (combining strings)

first_name = 'Zack'
last_name = 'Goodger'
full_name = first_name + ' ' + last_name
print(full_name)

# Lists, a list stores a series of items in a particular order. You acess items using an index, or within a loop. 

# make a list

cereals = ['coco pops', 'frosties', 'weetabix']

# get the first item in a list:

first_cereal = cereals[0]

# get the last item in a list:

last_cereal = cereals[-1]

# looping through a list:

for cereal in cereals:
    print(cereal)

# adding items to a list: 

cereals = []
cereals.append['shreddies']
cereals.append['corn flakes']
cereals.append['cheerios']

# making a numerical list:

squares = []

for x in range(1,11):
    squares.append(x**2)

# slicing a list:

finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]

# copy a  list:

finishers_copy = finishers[:]

# Tuples are similar to lists, but the items cannot be modified:

dimensions = (1920,1080)

# if statements are used to test for particular conditions and respond appropriately. 

# equals x == 42 
# not equal x ! = 42 
# greater than x > 42 
# greater than or equal to x > = 42 
# less than x < 42 
# less than or equal to x < = 42

# conditional test with lists:

'cheerios' in cereals
'surly' not in cereals 

# assigning boolean values:

game_active = True
can_edit = False

# a simple if test: 

if age < 4:
    ticket_price = 0 
elif age < 18:
    ticket_price = 10 
else:
    ticket_price = 15 

# Dictionaries store connections between pieces of information. Each item in a dictionary is a key-value pair. 

alien = {'colour': 'Green', 'points': '5'}

# Access a value:

print("The Aliens colour is" + alien['colour'])

# Adding a new key-value pair:
alien['x_position'] = 0 

# looping through all Key-Value Pairs: 

fav_numbers = {'eric': 17, 'ever': 4, }
for name, number in fav_numbers.items():
    print(name + ' Loves ' + str(number))
# outputs:
# eric Loves 17
# ever Loves 4 

# Looping through all keys 

for name in fav_numbers.keys():
    print(name + ' loves a number ')

# will print eric loves a number, ever loves a number 

# Looping through all the values: 

for number in fav_numbers.values():
    print(str(number) + ' is a favourite')

# will print 17 is a favourite and 4 is a favourite 

input_name = input("What is your name?")
print("Hello " + input_name )

# Prompting for a numerical value: 

input_age = input("How old are you?")
input_age = int(input_age)

pi = input("What's the value of Pi? ")
pi = float(pi)

# while loops 

# a while loop repeats a block of code as long as a certain condition is true. 

# A simple while loop:

current_value = 1 
while current_value <=5:
    print(current_value)
    current_value +=1 

# letting the user choose when to quit
msg = ''
while msg != 'quit': # ! = 
    msg = input("What's your message? ")
    print(msg)

# functions

# functions are named blocks of code, designed to do one specific job. information passed to a function is called an argument
# information received by a function is called a parameter.

# a simple function

def greet_user():
    """Display a simple greeting"""
    print("Hello!")
greet_user

# Passing an argument 

def greet_user2(username):
    """Display a personalized greeting."""
    print("Hello, " + username + "!")
greet_user2('Jesse')

# default values for paramaters:
def make_pizza(topping='bacon'): 
    """Make a single-topping pizza.""" 
    print("Have a " + topping + " pizza!") 
    
make_pizza() 
make_pizza('pepperoni')

def add_numbers(x, y): 
    """Add two numbers and return the sum.""" 
    return x + y 

sum = add_numbers(3, 5) 
print(sum)

# Classes 

# A class defines the behaviour of an object and the kind of information an object can store.

# The information in a class is stored in attributes, and functions that belong to a class are stored in methods 

# a child class inherits the methods and attributes from its parent class 

class Dog():
    """Represent a dog."""

    def __init__(self, name):
        """Initialize dog object."""
        self.name=name 
    def sit(self):
        """Simulate sitting."""
        print(self.name + " is sitting.")

my_dog = Dog('Peso')
print(my_dog.name + " is a great dog!")
my_dog.sit 

class SARDog(Dog): 
    """Represent a search dog.""" 
    def __init__(self, name): 
        """Initialize the sardog."""
    super().__init__(name) 
    def search(self): 
    """Simulate searching.""" 
    print(self.name + " is searching.") 
my_dog2 = SARDog('Willie') 
print(my_dog2.name + " is a search dog.") 
my_dog2.sit() 
my_dog2.search()

