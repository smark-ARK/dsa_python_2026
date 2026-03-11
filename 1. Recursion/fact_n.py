def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


#  take input from the user
n = int(input("Enter a number: "))
# call the function and print the result with a message
print(f"The factorial of {n} is: {fact(n)}")
