decimals = range(0, 100)
my_range = decimals[3:40:3]
print(my_range == range(3, 40, 3))
print(range(0, 5, 2) == range(0, 6, 2))  # even though parameters are different, these ranges result into sequence
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

r = range(0, 100)
print(r)
print("r[-2]={}".format(r[-2]))  # start from an end by going back
for i in r[::-2]:  # going back
    print(i)
print(r[::-2])  # identical to range(99,0,-2)

print(range(0, 100)[::-2] == range(99, 0, -2))

# reverse a string
backString = "egaugnal lufrewop yrev a si nohtyP"
print(backString[::-1])

r = range(0, 10)
# reverse
for i in r[::-1]:
    print(i)

# tadaa
test = [i for i in r[::-1]]
print(test)
