a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b:
    a, b = b, a 
if a > c:
    a, c = c, a 
if b > c:
    b, c = c, b

print("Ordered numbers: ", a, b, c)