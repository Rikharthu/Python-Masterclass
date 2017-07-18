for i in range(1, 15):
    # for scope
    if (i > 9):
        # if scope
        print("Large number")
    print("No {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
print()
# Instead of braces {...} Python uses indentations are used for scopes

# read input
name = input("Please enter your name: ")
age = int(input("How old are you, {}?\n".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
elif age >= 8:  # else if
    print("You are old enough to go to school")
else:
    print("You are too young. Please come back in {} years".format(8 - age))

# Advanced conditions
if age >= 16 and age <= 65:
    print("Have a good day at work")
# Or:
if 16 <= age <= 65:
    print("Don't forget to buy milk!")

if age < 16 or age > 65:
    print("Enjoy your free time")

print()

x = "false"
if x:
    # in Python all non-empty and non-zero values will evaluate into 'true'
    print("x is true")

y = True
if (y):
    y = False
    y = not y
    print(y)

# Inspect
print("""False: {}
None: {}
0: {}
0.0: {}
empty list []: {}
empty tuple (): {}
empty string '': {}
empty string \"\": {}
empty mapping {{}}: {}
""".format(False,
           bool(None),
           bool(0),
           bool(0.0),
           bool([]),
           bool(()),
           bool(''),
           bool(""),
           bool({}))
      )
# Spoiler: all will be False

x = input("Please enter some text: ")
# check if user did write something
if x:
    # P.S. if user writes 0, it is still true, sine 0 from input() will be read as "0" (string)
    print("You entered '{}'".format(x))
else:
    print("You did not enter anything")

if not (age < 18):  # not = !<statement>
    print("You are old enough to vote")
else:
    print("Please come back in {} years".format(18 - age))

parrot = "Norwegian Blue"
letter = input("Enter a character: ")
if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter")
