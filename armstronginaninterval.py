lower = int(input('Enter lower range: '))
upper = int(input('Enter upper range: '))
print('Armstrong numbers between', lower, 'and', upper, 'are:')
for num in range(lower, upper + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)
# The above code will print all Armstrong numbers between the given interval.
