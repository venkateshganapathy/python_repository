"""
loops program
"""

#simple for loop
for i in 1,2,3:
    print(i)

#nested for loop
for day in "Mon", "Tue":
    for letter in day:
        print(letter)
        
#same above nested loop is rewritten using _ and __
#for _ in "Monday", "Tuesday", "Wednesday":
#    for __ in day:
#        print(__)


#while loop for factorial calculation which is the product of all the integers
#up to and including a given number

input_number = int(input("Dear user, enter the number for which factorial is needed "))

f = 1
while input_number > 0:
    f = f*input_number
    input_number-=1

print ("factorial is {} ".format(f))


