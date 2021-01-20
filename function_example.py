# calculate number of cans required to paint the wall

import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

'''
math.ceil() -> it gives the next height value of a decimal value 
eg -> ceil(1.2) = 2

round is not used here because we want a while no. while rounds gives a floating type number.
'''

