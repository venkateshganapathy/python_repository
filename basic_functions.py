""" Basic functions

"""

#Absolute Value
print("absolute value of -1 is ", abs(-1))

#bin function to provide binary value
print("binary value of 5 is ", bin(5))

#chr function to convert to characrter
print("convertion of 97 to a character gives ", chr(97))

#len function
print("length of word hello world is ", len('hello world'))

#max, min functions
print('max of 1,5,2,6,2 is ', max(1,5,2,6,2))
print('min of 1,5,2,6,2 is ', min(1,5,2,6,2))

#open a file and write 5 lines
myfile = open("my.txt", 'w')
i=0
while i<5:
    myfile.writelines("line number " + str(i))
    i += 1
myfile.close()

#open existing file and read all lines
myfile = open("my.txt", 'r') #'r' is the default action, so no need to mention
while True:
        line = myfile.readline()
        if line == '':
            break
        print(line, "\n")  #not sure why the new line character is NOT working?

#use For loop iterator to read all lines is a convenient way.
#This approach uses the fact that the file object includes an "iterator" that automatically
#returns all the lines in the file and stops at the end of the file, without us having
#to explicitly look for EOF. Many objects in Python have iterators. e.g. for letter in "word"

myfile = open('my.txt', 'r')
for line in myfile:
    print(line)
myfile.close()

        
