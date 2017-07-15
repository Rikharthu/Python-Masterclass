__author__ = "Rikharthu"

# https://pyformat.info/
print("For more info see https://pyformat.info/\n")

age = 21
# print("My age is "+age) # Error, there is no implicit conversion
# explicitly convert int to a string
print("My age is " + str(age) + " years")
# 2nd approach
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "January", "March", "May", "July", "August", "October", "December"))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}"""
      .format(28, 30, 31))

# !!! Old format in Python 2, try to avoid using it !!!
print("My age is %d years" % age)
print("My age is %d %s and %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))  # a**b a in power of b

# With new format:
print("\nUsing Python3 format:")
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))  # a**b a in power of b
    # print("No. {:>2} squared is {:>4} and cubed is {:>4}".format(i, i ** 2, i ** 3))  # will also works, since we pass arguments in correct order
# {0} 0 is not required if arguments are passed in correct order: {}
# {:>4} provides 4 space, aligns right. {:4} aligns right too, {:<4} aligns left

# Precision
# old format
print("Pi is approximately %.50f" % (22 / 7))
# new format
print("Pi is approximately {:.50}".format(22 / 7))
print("Pi is approximately {:20.5}".format(22 / 7))
