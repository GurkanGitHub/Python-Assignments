number = int(input("enter a number to check if it is a prime number"))

count = 0

for i in range(1, number+1):
    if not (number % i):count += 1

if (number == 0) or (number == 1) or (count >=3):
    print(number, " is not a prime number.")
else:
    print(number, "is a prime number")
