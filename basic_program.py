x = 5
square = lambda x:x*x
print(square(5))
mylist = [(1,5),(2,50),(6,8),(-3,0)]
mylist.sort(key=lambda x:x[0])
print(mylist)

"""def decorator(f):
    def _f(x):
        print("I'm in f, calling", f, "with argument", x)
        return f(x)
    return _f
@decorator
def g(x):
    print("I'm in g with argument", x)

g(42)


def func (*args, **kwargs):
    print ("Args: ", args)
    print ("Keyword args: ", kwargs)

func(10,11,12, a='4', b='5')

def fibonacci(n):
    if n ==0:
        return 0
    fc = fn = 1
    for _ in range(2,n):
        fn, fc = fc + fn, fn
        print(fn)
    return fn

print(fibonacci(10))


mylist = ['this', 'is', 'a', 'great','opportunity']
print(mylist[1:3])


myfile = open("my.txt", 'w')
i=0
while i<5:
	myfile.writelines("line number " +str(i))
	i+=1
myfile.close()
myfile = open('my.txt', 'r')
            
while True:
              line = myfile.readline()
              if line == '':
                  break
              print(line)
myfile.close()

for letter in "wordpress":
    print(letter)

if 4 == 2/2:
    print("4= 2/2!")
else:
    print("4# 2/2!")

for x in 1,2,3:
    print(x)

#Fibonacci numbers are defined with this function fn = fn-1 + fn-2 with seed values f0=0 and f1=1
given_number = 10
fibo = [0,1]
for n in range(2, given_number+1):
    fibo.append(fibo[n-1]+fibo[n-2])
print(fibo[given_number])

#sine of any random value x (in radians) using this Taylor series
#sin x = x- x**3/3! + x**5/5!... for all x

months = {"Jan":"31", "Feb":"28", "Mar":"31", "Apr":"30"}
month_name = input("Enter month name: ")
print(months[month_name])

"""
    




