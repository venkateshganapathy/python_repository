""" lists and tuples

"""

mylist = ["this", "is", "my", "list"]   #note list has square brackets
mytuple = ("this", "is", "my", "list")  #note tuple has parantheses

for item in mylist:
    print(item)

print('\n')

# -1 refers to last position in the list, -2 is the penultimate and so on
i = -1
while i >= -4:
    print( mylist[i])
    i -= 1

#take pieces out of the list, using a notation called slicing
print(mylist[1:3])
#mylist[i:j] is a slice that selects all items with index k such that i<= k < j.

#some built in methods to use with lists and tuples
print("all([0,1,2]) ", all([0,1,2]))  #returns True if all list items evaluate to True
print("any([0,1,2]) ", any([0,1,2]))  #returns True if any list items evaluates to True
print("len([0,1,2]) ", len([0,1,2]))
print("min([0,1,2]) ", min([0,1,2]))
print("max([0,1,2]) ", max([0,1,2]))
print("sum([0,1,2]) ", sum([0,1,2]))
print("range([6]) ", range(6))
print("map(str, range[5]) ", map(str, range(5))) #retunrs a list of integers converted to strings
print("filter(bool, range[5])", filter(bool, range(5))) #returns a list of only those items that evaluate to True




