#Importuje bibliotekę NumPy
import numpy as np

#Pyta o nazwę pliku
fname1 = input("Enter file of first matrix: ")

#Pyta o nazwę pliku
fname2 = input("Enter file of second matrix: ")

#Tworzy warunek dotyczący nazwy pliku 
if len(fname1) < 1 : fname1 = "matrix1.txt"

#Tworzy warunek dotyczący nazwy pliku 
if len(fname2) < 1 : fname2 = "matrix2.txt"

#Tworzy Macierz 1
i1 = np.loadtxt(fname1, dtype='i', delimiter=',')
#Tworzy Macierz 2
i2 = np.loadtxt(fname2, dtype='i', delimiter=',')
print("Matrix 1 : ")
print(i1)
print("Matrix 2 : ")
print(i2)

#Oblicza iloczyn skalarny macierzy
dotproduct = np.dot(i1, i2)
print("Dot product of two array is : ")
print(dotproduct)