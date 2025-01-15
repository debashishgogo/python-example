def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return (x * factorial(x-1))
num = int(input('Enter a number: '))
if num < 0:
    print('Factorial does not exist for negative numbers')
elif num == 0:
    print('The factorial of 0 is 1')
else:
    print('The factorial of', num, 'is', factorial(num))
# The above code will find the factorial of a given number using recursion.