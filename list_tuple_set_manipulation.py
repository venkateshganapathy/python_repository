#List, Tuples, Sets manipulation 

my_list1 = [1,2,3]
my_list2 = [4,5,6]
print(my_list1 + my_list2)

#duplicate list items by using *
my_friends_list = ['friend']*3

#append an item to the list
my_friends_list.append("new friend")
print(my_friends_list)

#to count the number of items matching given value
print(my_friends_list.count("friend"))

#return the index number of item x, if found in the list
print(my_friends_list.index("new friend"))

#to remove and return item at index x (default last)
my_friends_list.pop() #will remove last item in the list
print(my_friends_list)

#to remove the first occurence of item with the value x  remove(x)
my_friends_list.remove('friend')
print(my_friends_list)

#to reverse the order of the items in the list
my_friends_list.reverse()
print(my_friends_list)

#to sort the items in the list, optionally using the key function "key" and/or in reverse ord
my_friends_list.extend(["my new friend2", "my new friend3", "my new friend0"])
my_friends_list.sort(reverse=True)
print(my_friends_list)

