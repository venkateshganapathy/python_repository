"""
math_ops.py
square, cube division and modulus operations for given two numbers
for the given two numbers, this program prints square, cube, division
and modulus operations
"""

input_number = input("Dear user, enter two numbers separated by comma or space ")
if (len(input_number.split(','))== 2):  #means user has separated input by comma
    input_list = input_number.split(',')
elif (len(input_number.split(' '))== 2):  #means user has separated input by space
    input_list = input_number.split(' ')
else:
    print ("invalid input")
    input_list = 0

if (input_list !=0):
    print("First number is {}".format(input_list[0]))
    print("-----------------------------")
    print("its Sauare value {}".format(int(input_list[0])**2))
    print("its Cube value {}".format(int(input_list[0])**3))
    print("-----------------------------")
    print("Second number is {}".format(input_list[1]))
    print("-----------------------------")
    print("its Sauare value {}".format(int(input_list[1])**2))
    print("its Cube value {}".format(int(input_list[1])**3))
    
    print("-----------------------------")
    print("Division of first number by second number is {}".format(int(input_list[0])//int(input_list[1])))
    print("-----------------------------")
    print("Modulus of first number by second number is {}".format(int(input_list[0])%int(input_list[1])))
    print("-----------------------------")
