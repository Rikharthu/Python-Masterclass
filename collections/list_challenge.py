menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

print(menu)

# print all meals that do not have spam
for meal in menu:
    if not "spam" in meal:
        print("Meal: {}".format(meal))
        for ingredient in meal:
            print(ingredient, end=" ")
        print()

no_spam = [meal for meal in menu if not "spam" in meal]
print(no_spam)
