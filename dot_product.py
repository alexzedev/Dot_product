#Importing NumPy library
import numpy as np

#Asking for input file
fname1 = input("Enter file of first matrix: ")

#Asking for input file
fname2 = input("Enter file of second matrix: ")

#Make conditional statement about file name
if len(fname1) < 1 : fname1 = "matrix1.txt"

#Make conditional statement about file name
if len(fname2) < 1 : fname2 = "matrix2.txt"

#Create Matrix 1
i1 = np.loadtxt(fname1, dtype='i', delimiter=',')
#Create Matrix 2
i2 = np.loadtxt(fname2, dtype='i', delimiter=',')
print("Matrix 1 : ")
print(i1)
print("Matrix 2 : ")
print(i2)

#Calculate dotproduct of the Matrix
dotproduct = np.dot(i1, i2)
print("Dot product of two array is : ")
print(dotproduct)