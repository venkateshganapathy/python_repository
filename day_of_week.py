"""
displaying day of the week
this program get a number from user and print the respective day of the week.
valid inputs numbers are 1 to 7. if user enters any other number, program
prints invalid input
"""

input_number = input("Dear user, enter the number between 1 and 7: ")

while input_number != '0':
    if input_number=='1':
        print("Monday")
    elif input_number =='2':
        print("Tuesday")
    elif input_number =='3':
        print("Wednesday")
    elif input_number =='4':
        print("Thursday")
    elif input_number=='5':
        print("Friday")
    elif input_number=='6':
        print("Saturday")
    elif input_number=='7':
        print("Sunday")
    else:
        print("invalid input number")
    input_number = input("Dear user, enter the number between 1 and 7: ")
    print("input_number {}".format(input_number))

print("Program reached end state")

