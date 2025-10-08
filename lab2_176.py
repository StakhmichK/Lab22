n = int(input("Enter 4-digit number: "))

a = n // 1000         
b = (n // 100) % 10    
c = (n // 10) % 10     
d = n % 10        

if a % 2 == 0:
    a = '*'
else:
    a = str(a)

if b % 2 == 0:
    b = '*'
else:
    b = str(b)

if c % 2 == 0:
    c = '*'
else:
    c = str(c)
if d % 2 == 0:
    d = '*'
else:
    d = str(d)

result = a + b + c + d
print("Result is: ", result)