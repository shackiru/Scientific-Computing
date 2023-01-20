import numpy as np

matrix1 = np.array([[1,2], 
                    [3,4]])

matrix2 = np.array([[5,6] ,
                    [7,8]])

#print(matrix1 + matrix2)
#print(matrix1 * matrix2)
#print(np.dot(matrix1, matrix2))

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#print(array[3:6])
#print(array[3:6 -1])
#print(array[: : -1])

#untuk tujuan 1 - 9, sebanyak 5 kali
linspace = np.linspace(1, 9, 5)
#print(linspace)

#buat ngecek plus minus, plus = 1, minus = -1, 0 = 0
#print(np.sign(-4))
#print(np.sign(10))
#print(np.sign(array))

#absolute, ngebalikin angka negatif jadi positif
#print(np.abs(array))

#untuk resize array
array.resize(2,4)
#print(array)


#untuk horizontal stack
array = np.hstack(array)
print(array)

#untuk vertical stack
array = np.vstack(array)
print(array)
