n = (input("Enter 4-digit number: ")).strip()
result = ""
for digit in n:
        if int(digit) % 2 == 0:
                result += "*"
        else:
                result += digit
print("Your number is: ", result)