number = int(input("Enter number : "))
factorial = 1
if number < 0:
    print("Error")
elif number == 0:
    print("Factorial of 0 is", 1)
else:
    for i in range(1, number+1):
        factorial = factorial*i

    print("factorial of", number, "is", factorial)
