
print ("This is 3rd commit file to the new branch")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get user input
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))
