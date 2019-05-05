#read from file and sort contents

#read data from file
f = open("emp_name_data.txt")

#store each line / name in the list
names_list = f.read().splitlines()

#sort the names_list using a lambda function
names_list.sort()
print(names_list)


#square = lambda x:x*x
#which is exactly the same as defining a square function like this
# def square(x):
    #return x*x
