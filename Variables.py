greeting = "Hello"
Greeting = "Greetings"  # case-sensitive
name = "Bruce"
print(name)
name = 5  # not an error
print(name)

_myName = "Bob"
_myName2 = "Jack"

# TODO
# FIXME

age = 21
print(age)  # OK
# print(greeting+age) #error, age is expected to be a string, since theres no implicit conversion
print(greeting + age.__str__())  # OK
print("Hello " + str(24))
# Numbers
import sys

a = 13
print("{0} in binary is {1}, it's size is {2} bytes and type is {3}"
      .format(a, bin(a), sys.getsizeof(a), type(a)))
print("Max int size is {0}".format(sys.maxsize))
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # returns a float
print(a // b)  # 4, returns as a whole number
print(a % b)  # 1, remainder

for i in range(1, a // b):
    print(i)

c = a + b
d = c / 3
e = d - 4
print(e * 12)
print(type(e))

# === Strings ===
parrot = "Norwegian Blue"
print("{0} is a {1}, it's size is {2} bytes, length is {3}"
      .format(parrot, type(parrot), sys.getsizeof(parrot), parrot.__len__()))
# get separate characters at given positions
print(parrot)
print(parrot[0])
print(parrot[3])
# loop through string's characters
for c in parrot:
    print(c)
# negative index start counting in reverse position, starting from the end
print(parrot[-1])  # e  (Norwegian Blu*e*)
print(parrot[-2])  # u (Norwegian Bl*u*e)
# get range:
print(parrot[0:6])  # Norweg
# extract substring starting from #6 til the end of the string
print(parrot[6:])  # ian Blue
print(parrot[-4:-2])  # Bl
# starting from position #0 extract all characters up to an index # non-inclusive
# with a step of 2
print(parrot[0:6:2])  # Nre ('N'o'rw'e'g)
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4])  # ,,,,,,
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])  # 123456789

string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("he's probably" + " pining")
print("Hello " * 5)  # Hello Hello Hello Hello Hello
string1 *= 5
print(string1)  # he's he's he's he's he's
today = "Friday"
# check if "Friday" contains a substring "day"
print("day" in today)  # True
print("parrot" in "fjord") # False
