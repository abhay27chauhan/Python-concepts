# check here - https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

# importing random module
import random

randomInteger = random.randint(1, 10) 
print(randomInteger)

randomFloat = random.random() * 5  # it gives value b/w 0 and 1 (not including 1). After multiplying by 5 it gives b/w 0 and 5 (not including 5)
print(randomFloat)
