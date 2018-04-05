from test2 import grocery_list
from test4 import super_villains

for x in (1, 2, 3, 5, 4, 3):
    print(x, end="")

print()

for x in range(1, 9):
    print(x, ',',  end="")

print()

for x in grocery_list:
    print(x, '', end="")

for x in super_villains:
    print(x)
    print(super_villains[x])

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])
