num = int(input('Enter a number: '))    
if num == 0 or num == 1:
    print('{0} is not a prime number'.format(num))
else:    
    for i in range(2, num):
        if (num % i) == 0:
            print('{0} is not a prime number'.format(num))
            break
    else:
        print('{0} is a prime number'.format(num))
    

    