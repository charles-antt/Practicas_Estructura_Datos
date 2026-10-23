a = [[1,2],
     [3,4]]
b = [[5,6],
     [7,8]]

suma = [[a[i][j] + b[i][j] for j in range (len(a[0]))] for i in range(len(a))] 
print(suma)