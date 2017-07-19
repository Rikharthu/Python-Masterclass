# Iterable is an object that is capable of returning it's members one at a time
# Iterables are: string, list....

string = "1234567890"
for char in string:  # string is actually implicitly converted to iter(string)
    print(char, end=", ")
print()
# upper example is actually as follows:
for char in iter(string):
    print(char, end=", ")
print()

# iterator approach
iterator = iter(string)
print(iterator)  # object
# print elements
print(next(iterator), end=", ")
print(next(iterator), end=", ")
print(next(iterator), end=", ")
print(next(iterator), end=", ")
print(next(iterator), end=", ")
print(next(iterator), end=", ")
print(next(iterator), end=", ")
print(next(iterator), end=", ")
print(next(iterator), end=", ")
print(next(iterator))
# print(next(iterator)) # Error, no more elements
