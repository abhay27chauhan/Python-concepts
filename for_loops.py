# For Loop with Lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(fruits)

# using range function

even_sum = 0
for number in range(2, 101, 2): # here becoz of 3rd parameter the sequence will be 2, 4, 6, 8
  # print(number)
  even_sum += number
print(even_sum)

#or

alternative_sum = 0
for number in range(1, 101):
  if number % 2 == 0:
    # print(number)
    alternative_sum += number
print(alternative_sum)

# example - combination of both types

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")
