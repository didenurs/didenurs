# find factorial of a number

def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

x = int(input("Please enter the number: "))
print("The result of the factorial of ", x, "is equal to23 = ", factorial(x))