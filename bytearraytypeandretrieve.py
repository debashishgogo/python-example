elements = [10, 20, 0, 40, 15]
x = bytearray(elements)
x[0] = 88
x[1] = 99
for i in x:
    print(i)