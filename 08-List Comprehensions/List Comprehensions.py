x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Using list comprehensions to generate the coordinates
coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

# Sorting the coordinates in lexicographic increasing order
coordinates.sort()

# Printing the coordinates
print(coordinates)