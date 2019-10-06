#Dictionaries

phone_dir = {"Bob":"212­555­1212",
     "Ted":"214­555­1212",
     "Carol":"416­555­1212", "Alice":"514­555­1212"}
print(phone_dir)

one100squares = {k:k**2 for k in range(100)}
print(one100squares.get(99))

square_and_cube_d = dict((k, k**2) for k in range(5))
print(square_and_cube_d)
square_and_cube_d.update((k, k**3) for k in range(3, 7))
print(square_and_cube_d)
for k in square_and_cube_d:
    print(k)

#is key 100 in one100squares
print(100 in one100squares)
print(99 in one100squares)
print(len(one100squares))
print(one100squares[4])
del one100squares[20]
print(len(one100squares))
print(one100squares.get(20, 'Not Found'))
print(one100squares.get(21, 'Not Found'))
print(square_and_cube_d.items())
print(square_and_cube_d.keys())
print(square_and_cube_d.values())
