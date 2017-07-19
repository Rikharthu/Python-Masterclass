my_range = range(100)  # [0, 100) == [0, 99]
print("my_range is {}".format(type(my_range)))
print(my_range)  # range(0, 100)

# create a list from a range
my_list = list(my_range)
print(my_list)

# range iterator
range_iterator = iter(my_range)
length = len(my_range)
for i in range(0, length):
    print(next(range_iterator), end=", ")
print()

even = list(range(0, 10, 2))  # third parameter is step
odd = list(range(1, 10, 2))
print(even)
print(odd)

# ranges are efficient. both those ranges use exactly the same amount of memory
small_range = range(0, 10)
large_range = range(0, 100000000)
import sys

print("small_range size: {} bytes".format(sys.getsizeof(small_range)))
print("large_range size: {} bytes".format(sys.getsizeof(large_range)))
# which is not the case for lists:
small_list = list(small_range)
large_list = list(large_range)
print("small_list size: {} bytes".format(sys.getsizeof(small_list)))
print("large_list size: {} bytes".format(sys.getsizeof(large_list)))

my_string = "abcdefghijklminitasdyas"
print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0, 10)
print(small_decimals)
print(small_decimals.index(3))
print(small_decimals[3])

odd = range(1, 10000, 2)
print(odd)
print(odd[985])
print(1971 in odd)
print(1972 in odd)

# modify original range
# add step
my_range = small_decimals[::2]
print(my_range)
my_range = small_decimals[1::2]
print(my_range)

# take a slice from a range
my_range = large_range[3:40:3]
print(my_range)
for i in my_range:
    print(i)
print('=' * 40)
for i in range(3, 40, 3):
    print(i)

print(my_range==range(3, 40, 3))
