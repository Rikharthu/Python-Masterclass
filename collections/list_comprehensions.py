# from https://docs.python.org/3.3/tutorial/datastructures.html

# for instance we want to create a list of squares
# default approach:
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

# list comprehension approach:
squares = [x ** 2 for x in range(10)]
print(squares)
# This is also equivalent to squares = list(map(lambda x: x**2, range(10)))

# List comprehensions are used to make new lsits where each element is the result
# of some operations applied to each member of another sequence or iterable
# or to create a subsequence of those elements that satisfy certain conditions

# It consists of brackets containing an expression followed by a for clause
# the result will be a new list resulting from evaluating the expression in the context
# of the for and if clauses which follow it
# For example combine the elements of two lists if they are not equal
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(pairs)
# this is equivalent to
pairs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if (x != y):
            pairs.append((x, y))
print(pairs)

vec = [-4, -2, 0, 2, 4]
print(vec)
# create a new list with the values doubled
vec = [x * 2 for x in vec]
print(vec)
# filter the list to exclude negative numbers
vec = [x for x in vec if x >= 0]
print(vec)
# apply a function to all the elements
vec = [abs(x) for x in vec]
print(vec)
# call a method on each element
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
fruits = [fruit.strip() for fruit in freshfruit]
print(fruits)
# create a list of 2-typles (number, square)
tuples = [(x, x ** 2) for x in range(6)]
print(tuples)
# [x, x**2 for x in range(6)] Error! Tuple must be parenthesized

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(vec)
vec = [num for elem in vec for num in elem]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(vec)

# list comprehensions can contain complex expressions and nested functions
from math import pi

pis = [str(round(pi, i)) for i in range(1, 6)]
print(pis)

# Nested list comprehensions
print("\nNested list comprehensions")

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print("Given matrix: {}".format(matrix))
# transpose rows and columns
transposed = [[row[i] for row in matrix] for i in range(4)]
print("Transposed matrix: {}".format(transposed))
# equivalent to
# (the nested listcomp is evaluated in the context of the for that follows it)
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
# and
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
# P.S. build-in function for transposing matrix:
print(list(zip(*matrix)))
