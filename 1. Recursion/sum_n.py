def sum(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


# take input from the user
n = int(input("Enter a number: "))
# call the function and print the result with a message
print(f"The sum of numbers from 1 to {n} is: {sum(n)}")
