n = input("Enter a number (in XX.XX format): ")

parts = n.split(".")
whole = parts[0]
fraction = parts[1]

new_whole = fraction
new_fraction = whole

result = new_whole + "." + new_fraction
result_float = float(result)

if int(new_fraction) == 0:
    print("As a result, the fractional part became zero:", result_float)
else:
     print("New number: ", result_float)