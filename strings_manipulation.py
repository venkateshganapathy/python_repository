#strings manipulation

line1 = "first line"    #string for first line
line2 = "second line"   #string for second line
line3 = "third line"    #string for third line

"""
f = open("/tmp/3lines.txt", 'w') #open a file to write
f.write(line1 + '\n')           #write first line, append a new line
f.write(line2 + '\n')           #write second line, append a new line
f.write(line3 + '\n')           #write third line, append a new line
f.close()                       #close the file
"""
a='abcdd ab cd d  '
print("'a'+'b' :", 'a'+'b' , '\n')
print("'a' * 5 :", 'a' * 5 , '\n')
print("'a' in 'bac': ", 'a' in 'bac',  '\n')
print("a='abcdd ab cd d', a[1]= ", a[1],'\n')
print("a='abcdd ab cd d', a[2:4]= ", a[2:4], '\n')
print("a='abcdd ab cd d', a[-1]= ", a[-1], '\n')
print("'a='abcdd ab cd d', a.capitalize()= ", a.capitalize(), '\n')
print("'a=abcdd ab cd d', a.center(20)= ", a.center(20), '\n') #padded with blank with string centered
print("'a=abcdd ab cd d', a.find('cdd')= ", a.find('cdd'), '\n')
print("'a=abcdd ab cd d', a.upper()= ", a.upper(), '\n')
print("'a=abcdd ab cd d', a.partition('ab c'))= ", a.partition('ab c'), '\n') #splits the string at seperator given and returns a 3-tuple with the first part, the separator and the last part
print("'a=abcdd ab cd d', a.splits(' '))= ", a.split(' '), '\n')
print("'a=abcdd ab cd d  ', a.strip()= ", a.strip(), '\n')
      


      
      
