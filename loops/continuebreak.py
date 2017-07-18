shopping_list = ["milk", "pasta", "eggs", "spam", "beer", "bread", "rice"]
for item in shopping_list:
    if (item == "spam"):
        # skip this item
        continue
    if (item == "beer"):
        print("No alcohol! Create a new shopping list!")
        # Exit the loop
        break
    print("Buy " + item)

for i in range(1, 11):
    print(i, end=", ")
else:
    # else after 'for' statement marks a code, that will execute only after
    # 'for' loop successfully finished without exiting
    print("\nFinished counting to 10")

for i in range(1, 11):
    if i > 6: break
    print(i, end=", ")
else:
    # this won't run since 'for' loop wont finish
    print("\nThis won't run")
