"""
expression chaining
this program compares whether the given age value is valid by checking whether it
is between 0 and 115 using expressin chaining
"""

input_number = int(input("Dear user, enter your age here: \n"))

if (-1 < input_number < 116):
    print("Your age {} is a valid age".format(input_number))
else:
    print("Your age {} is not a valid age".format(input_number))
    
Adam = 34
Bella = 23
Ram = 90
Visuk = 90
Reva = 91


if (Adam < Ram == Visuk <= Reva >= Bella):
    print("Adam's age ({}) is less than Ram's age ({}) which is equal to Visuk's age ({}) which is less than or equal\ to Reva's age ({}) which is greater than Bella's age ({}).".\
          format(Adam, Ram, Visuk, Reva, Bella))

"""following statement just works fine even though the variables buffalo and bill are not defined.
Python valuates only what needs to be evaluated. In this case 1>2 is false hence it doesnt go further to those 2 undefined variables and don't throw any error"""
if 1 > 2 < buffalo <bill:
    print("shouldn't get here")

"""Conditional Expression assignment"""
b=49502
a = 1 if b<5 else b
print ("a = {}".format(a))

print("program reached end state")    
