# Dictionaries are collections that are accessed by keys rather than indexes (Map)

# initializing a dictionary
fruit = {"orange": "a sweet, organge, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green, citrus fruit",
         "apple": "round and crunchy"}  # override/update
print(fruit)
print(type(fruit))

# access individual items through keys
orangeDescription = fruit["orange"]
grapeDescription = fruit["grape"]
print(orangeDescription)
print(grapeDescription)

# unexisting key
# cabbageDescription=fruit["cabbage"] # error
cabbageDescription = fruit.get("cabbage")  # wont crash, returns "None"

# multiple types
bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": 250}
print(bike)
print("Honda" in bike) # value existence - False
print("make" in bike) # key existence - True

# add new item to a dictionary
fruit["pear"] = "an odd shaped apple"
print(fruit["pear"])
# replace existing value
fruit["pear"] = "a really odd shaped apple, great with tequilla"
print(fruit["pear"])

print(fruit)
# delete and enty
del fruit["lemon"]
print(fruit)
# delete entiry dictionary
# del fruit
# print(fruit) will be an error now

while True:
    dict_key = input("Please enter a fruit: ")
    if (dict_key == "quit"):
        break
    if dict_key in fruit:  # check if has key
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we don't have a " + dict_key)

# clear entire dictionary
fruit.clear()
print(fruit)
