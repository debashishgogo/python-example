num = int(input('Enter a number: '))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, 'is an Armstrong number')
else:
    print(num, 'is not an Armstrong number')
# The above code will check if a given number is an Armstrong number or not.
