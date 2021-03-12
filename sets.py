set_var = set()
print(set_var)
print(type(set_var))

set_var = {1, 2, 3, 4, 3}
print(set_var)

set_var = {"Avengers", "IronMan", 'Hitman'}
print(set_var)

# adding to set
set_var.add("Hulk")
print(set_var)

# intersection -> returns the intersection b/w 2 sets
set1 = {"Avengers", "IronMan", 'Hitman'}
set2 = {"Avengers", "IronMan", 'Hitman', 'Hulk2'}

inter = set1.intersection(set2)
print(inter)

# intersection_update
set2.intersection_update(set1)  # updates set2 with the intersection
print(set2)

# difference
set1 = {"Avengers", "IronMan", 'Hitman'}
set2 = {"Avengers", "IronMan", 'Hitman', 'Hulk2'}

diff = set2.difference(set1)
print(diff)

# diffrence_update
set2.difference_update(set1) # updated set2 with difference value
print(set2)
