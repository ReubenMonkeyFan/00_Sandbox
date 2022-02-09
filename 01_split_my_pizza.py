# ask and store the amount of slices and people
try:
    slice_number = int(input("How many slices of pizza are there? "))
    print()
    print("You have said there are {} slices of pizza.".format(slice_number))
    print()
except ValueError:
    print()
    slice_number = int(input("How many slices of pizza are there? Please answer in a whole number. "))
    print()
    print("You have said there are {} slices of pizza.".format(slice_number))
    print()

try:
    people_number = int(input("How many people are sharing the pizza? "))
    print()
    print("You have said there are {} people having pizza.".format(people_number))
    print()
except ValueError:
    print()
    people_number = int(input("How many people are sharing the pizza? Please answer in a whole number. "))
    print()
    print("You have said there are {} people having pizza.".format(people_number))
    print()

# calculate the amount of slices per person and leftover slices
slice_per_person = slice_number // people_number

leftover_slices = slice_number % people_number

#tell the user the amount of slices per person and leftover slices

print("Each person will recieve {} slices of pizza.".format(slice_per_person))
print()
print("There will be {} leftover slices.".format(leftover_slices))







