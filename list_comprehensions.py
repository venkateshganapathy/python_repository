"""list comprehensions
python offers a concise way to build lists and other objects using comprehensions

"""

mylist = [i**2 for i in range(100)]
print(mylist)

#nested comprehensions
mysecondlist = [(i,j) for i in range(4) for j in range(6)]
print(mysecondlist)

mytuple =tuple(i**2 for i in range(4))  #note the word tuple is explicitly to be used for tuples
print(mytuple)

mytuple2 = tuple([i,j] for i in range(2) for j in range(3) if (i+j) % 3 !=0)
print(mytuple2)

#the same above for a list is written like the following
mylist3 =[[i,j] for i in range(2) for j in range(3) if (i+j) % 3 !=0]
print(mylist3)
