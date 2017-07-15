print("Hello World!")
# This is a comment
print(1+2)
print(7*6)
print() # empty line
print("The End")
print("Python's strings are easy to use")
print('We can even include "Quotes" in strings.\nOnly requirement is their type must be different.')
print("Hello "+"Brave "+"New"+" World")

# For loop
for i in range(10):
    print("count is {0}".format(i)) # similar to String.format(...)

greeting="Hello"
name="Bruce"
print(greeting+", "+name)

name=input("Please enter your name:\n")
print("{0}, {1}!".format(greeting,name))

splitString="This string has been\n\tsplit over\nseveral lines"
print(splitString)

print("1\t2\t3\t4\t5")

quotedString="The pet shop owner said \"No, no, 'e's uh,...he's resting\"" #escape quotes if both types of them are used
quotedStringV2='The pet shop owner said "No, no, \'e\'s uh,...he\'s resting"' #escape quotes if both types of them are used
print(quotedString)

# ''' will also work
anotherSplitString="""This string has been
split over
several lines"""
notSplitString="This string has not " \
               "been split over " \
               "several lines"
print(anotherSplitString)
print(notSplitString)