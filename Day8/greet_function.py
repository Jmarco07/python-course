# Function with no input

def greet():
    print("Hi there!")
    print("Welcome to the program.")
    print("This is a simple greeting function that prints a welcome message.")

greet()


# Function with input
def greet_with_name(name):
    print(f"Hi {name}!")
    print("Welcome to the program.")
    print("This is a simple greeting function that prints a welcome message.")

name = input("What is your name? ")
greet_with_name(name)

# Function with multiple inputs
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"WWhat is it like in  {location}.")

greet_with("Marco", "Philippines")

# Function with multiple inputs and using keyword arguments

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"WWhat is it like in  {location}.")

greet_with(location = "Philippines", name = "Marco")
