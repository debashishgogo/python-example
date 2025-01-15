def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print('The H.C.F. of', num1, 'and', num2, 'is', compute_hcf(num1, num2))
# The above code will find the H.C.F. of two numbers.
# In the above code, we have defined a function compute_hcf() which takes two arguments.
# The function returns the H.C.F. of two numbers.
# We have used the for loop to find the factors of both numbers and then find the common factors.
# The common factor is the highest common factor of the two numbers.
# The function returns the H.C.F. of the two numbers.
# We have taken two numbers as input from the user and passed them to the function.
# The function computes the H.C.F. of the two numbers and prints it.
# The output will be:
# Enter first number: 54
# Enter second number: 24
# The H.C.F. of 54 and 24 is 6
# In the above code, we have used the for loop to find the factors of both numbers.
