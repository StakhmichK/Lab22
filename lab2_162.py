bills = {
    1: "Volodymyr the Great",
    2: "Yaroslav the Wise",
    5: "Bohdan Khmelnytsky",
    10: "Ivan Mazepa",
    20: "Ivan Franko",
    50: "Mykhailo Hrushevsky",
    100: "Taras Shevchenko",
    200: "Lesya Ukrainka",
    500: "Gryhoriy Skovoroda",
    1000: "Volodymyr Vernadsky"
}
n =int(input("Enter the bill: "))
if n in bills:
     print(f"{n}, {bills[n]}")
else:
     print("No bill!")