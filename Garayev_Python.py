entered_number = int(input("Number: "))
if entered_number > 7:
    print("Hello")

entered_name = input("Name: ")
if entered_name == "John":
    print("Hello, John")
else:
    print("There is no such name")

numeric_array = input("Numbers: ").split()
for x in numeric_array:
    if int(x) % 3 == 0:
        print(x)