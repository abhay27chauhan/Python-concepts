# study different method on list here - https://docs.python.org/3/tutorial/datastructures.html

# python list documentation - https://developers.google.com/edu/python/lists#for-and-in

# example 1

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

num_of_states = len(states_of_america)

print(states_of_america[0])  # Delaware
print(states_of_america[num_of_states - 1]) # Hawaii
print(states_of_america[-1]) # Hawaii

states_of_america.append("Goa") # added to the last
states_of_america.extend(["Delhi", "Mumbai", "Hyd"]) # added these items to the last;

print(states_of_america)

# example 2

fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables] # nesting list inside list

print(dirty_dozen)

# example 3 

row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
