x = [[12, 7 ,3],[4 ,5 ,6],[7 ,8 ,9]]
y = [[5, 8 ,1,2],[6 ,7 ,3,0],[4 ,5 ,9,1]]
result = [[sum(a*b for a,b in zip(x_row,y_col)) for y_col in zip(*y)] for x_row in x]
for r in result:
    print(r)
# Output:
