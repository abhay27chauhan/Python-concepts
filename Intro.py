# 1 single line comment

'''
multiple line comment
'''

# 2 ways to print 
print("Welcome to the Band Name Generator.")

# 2.1 output with new line
print("hello")
print("peppers")

# 2.2 output without new line
print("Hello", end=" ")
print("peppers")


# 2.3 output without new line but with someother notation
print("Hello", end="->")
print("peppers")

# 2.4 output numbers and text
a = 4
b = 10
print("First Number: ", a, "and Second Number: ", b)

# 2.5 caution error
print("First Number: " + a + " and Second Number: " + b)

'''
File "Intro.py", line 29, in <module>
    print("First Number: " + a + " and Second Number: " + b);
TypeError: can only concatenate str (not "int") to str

'''

# 2.6 using format
first_name = "Abhay"
last_name = "Chauhan"

print("My first name is {} and last name is {}".format(first_name, last_name))

# can also be done as -
print("My first name is {first} and last name is {last}".format(first = first_name, last = last_name))

# 2.7 using f-String
print(f"My first name is {first_name} and last name is {last_name}")


# 3 taking input and saving to a variable
street = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")

# 4 concatination 
print("Your band name could be " + street + " " + pet)

# 5 Type 
two_digit_number = input("Type a Two digit Number:\n")

print(type(two_digit_number)) # str

# 6 geting a character from string
print(two_digit_number[0])
print(two_digit_number[1])

print(two_digit_number[0] + two_digit_number[1])

# 7 Type conversion
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

print(first_digit + second_digit)
