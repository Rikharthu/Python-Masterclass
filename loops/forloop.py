# For loops
print("\nFOR LOOPS")
for i in range(1, 21):  # [1:21)
    print("i is now {}".format(i))

# loop through each string character
message = "Hello World!"
for c in message:
    print(c)
print()

number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):
    if (not number[i] == ','):
        print(number[i], end='')  # avoid new line by specifying end character
print()
# or
for i in range(0, len(number)):
    if number[i] in "0123456789":
        print(number[i], end='')
print()

cleanedNumber = ''  # initialize variable
for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanedNumber += number[i]
print("The number is {}".format(cleanedNumber))

# Extended FOR loops
print("\nExtended FOR loops")

for state in ["not pinin", "no more", "a stiff", "bereft of lift"]:
    print("This parrot is " + state)

for i in range(0, 101, 5):
    print("i is " + str(i))

# Nested loops
for i in range(1, 13):
    for j in range(1, 13):
        print("{} times {} is {}".format(i, j, i ** j))
    print("|==============================|")
# or use \t as end character
for i in range(1, 13):
    for j in range(1, 13):
        print("{} times {} is {}".format(i, j, i ** j), end="\t")
    print()
