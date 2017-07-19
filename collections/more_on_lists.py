# Initialize lists
list1 = []
list2 = list()  # constructor

print("list1: {}".format(list1))
print("list2: {}".format(list2))
print("list1==list2? {}".format(list1 == list2))

# Iterable is an object that is capable of returning it's members one at a time
# lists can accept iterables as constructor parameters:
# string is an iterable
print(list("This is a list from a string"))  # list of each string's character

even = [2, 4, 6, 8]
another_even = even
another_even.sort(reverse=True)
# original 'even' list is modified
print("even: {}".format(even))
# this is because it is not creating a new object
print(even is another_even)
other_even = list(even)  # creates a new instance instead of pointing to an object
other_even.sort()
print("even: {}".format(even))
print("other_even: {}".format(other_even))

even.sort()
print("even == other_even? {}".format(even == other_even))
print("even is other_even? {}".format(even is other_even))

odd = [1, 3, 5, 7, 9]
numbers = [even, odd]  # [[2, 4, 6, 8], [1, 3, 5, 7, 9]]
print(numbers)

for number_set in numbers:
    print(number_set)

# concatenate both lists correctly and sort:
numbers = sorted(odd + even)
print(numbers)
