import numpy as np

A = np.random.randint(0,10, (3,3))

B = A.transpose()

C = np.dot(A,B)
print("Произведение матрицы")
print(A)
print("на матрицу")
print(B)
print("Результат: ")
print(C)


print("Теперь поменяем слагаемые местами и умножим вторую матрицу на первую")

print(np.dot(B,A))