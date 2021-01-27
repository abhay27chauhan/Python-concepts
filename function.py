# 1.1 Simple Function
def greet():  # declaring the function
  print("Hello Angela")
  print("How do you do Jack Bauer?")
  print("Isn't the weather nice today?")

greet() # calling the function


# 1.2 Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")

greet_with_name("Jack Bauer")


# 1.3 Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")


#Calling greet_with() with Positional Arguments -> sequence matters
greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")

#Calling greet_with() with Keyword Arguments -> sequence don't matter
greet_with(location="London", name="Angela")


# 1.4 returning the ouput instead of printing and Docstring

def format_name(f_name, l_name):
  """Take a first and last name and format it        
  to return the title case version of the name."""    # this is docstring -> description of function
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"


#Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)

#or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))
