# More info https://docs.python.org/3.3/tutorial/datastructures.html
# Section 4.6 https://docs.python.org/3/library/stdtypes.html
# TODO add examples from https://docs.python.org/3.3/tutorial/datastructures.html
# TODO and https://docs.python.org/3/library/stdtypes.html (examples, operator usages etc)

# ipAddress = input("Please enter an IP address: ")
# TODO for debug
ipAddress = "10.5.4.3.2.1"
print(ipAddress.count("."))

# create a list
parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]
# append items
parrot_list.append("drinking")
# will append each characted as a separate item, since string acts like a collection (see second link)
parrot_list += "flying"  # parrot_list=parrot_list+"flying" wont work
# print a list
print(str(parrot_list))
# iterate through a list
for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
# concatenate 2 lists
numbers = even + odd  # adds odd to the end of even
print(numbers)
numbers.sort()  # sort() works on an existing object, not creating new one
# if you wan't to create a new sorted object instead of mutating existing one, then use function:
numbers2 = sorted(numbers, reverse=True)  # sort reverse as specified by named parameter
print("Sorted:")
print(numbers)
print("numbers is a {}".format(type(numbers)))
print("Reverse:\n{}".format(numbers2))

vec = [-4, -2, 0, 2, 4]
doubled_vec = [x * 2 for x in vec]  # TODO what is 'for'in square brackets?
print(str(doubled_vec))
