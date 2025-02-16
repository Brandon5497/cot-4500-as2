import numpy as np

x = [3.6, 3.8, 3.9]
val = [1.675, 1.436, 1.318]
w = 3.7

nevile = np.zeros((3, 5))

nevile[:, 0] = val

for i in range(1, 3):  
    for j in range(1, i + 1):  
        term1 = (w - x[i - j]) * nevile[i][j - 1]
        term2 = (w - x[i]) * nevile[i - 1][j - 1]
        nevile[i][j] = (term1 - term2) / (x[i] - x[i - j])

print(f"Neville's method: {nevile[2][2]}\n")

x = [7.2, 7.4, 7.5, 7.6]
val = [23.5492, 25.3913, 26.8224, 27.4589]

diffs = np.zeros((4, 4))

diffs[:, 0] = val

for i in range(1, 4):  
    for j in range(1, i + 1): 
        diffs[i][j] = (diffs[i][j - 1] - diffs[i - 1][j - 1]) / (x[i] - x[i - j])

print(f"Newton's forward method:\n1st: {diffs[1][1]}\n2nd: {diffs[2][2]}\n3rd: {diffs[3][3]}")

approx = val[0] + (diffs[1][1] * (7.3 - x[0]))

print(f"\nf(7.3) = {approx}\n")

x = [3.6, 3.8, 3.9]
val = [1.675, 1.436, 1.318]
prime = [-1.195, -1.188, -1.182]

hermite = np.zeros((6, 5))

hermite[0][0] = 3.6
hermite[1][0] = 3.6
hermite[2][0] = 3.8
hermite[3][0] = 3.8
hermite[4][0] = 3.9
hermite[5][0] = 3.9

hermite[0][1] = 1.675
hermite[1][1] = 1.675
hermite[2][1] = 1.436
hermite[3][1] = 1.436
hermite[4][1] = 1.318
hermite[5][1] = 1.318

hermite[1][2] = -1.195
hermite[2][2] = (val[1] - val[0]) / (x[1] - x[0])
hermite[3][2] = -1.188
hermite[4][2] = (val[2] - val[1]) / (x[2] - x[1])
hermite[5][2] = -1.182


np.set_printoptions(linewidth = 200, formatter = {'float': lambda x: f"{x:.8e}"}, suppress=True)
print(f"Hermite polynomial approximation matrix:\n{hermite}\n")
np.set_printoptions(linewidth = 200, formatter = {'float': lambda x: f"{x:.8e}"}, suppress=False)

x = [2, 5, 8, 10]
val = [3, 5, 7, 9]
h0 = x[1] - x[0]
h1 = x[2] - x[1]
h2 = x[3] - x[2]

matrix = [[1, 0, 0, 0],
          [h0, 2 * (h0 + h1), h1, 0],
          [0, h1, 2 * (h1 + h2), h2],
          [0, 0, 0, 1]]

print("Matrix A:")
for row in matrix:
    print(f"[{' '.join(map(str, row))}]")

b1 = int((3 / h1) * (val[2] - val[1]) - (3 / h0) * (val[1] - val[0]))
b2 = int((3 / h2) * (val[3] - val[2]) - (3 / h1) * (val[2] - val[1]))

b = [0, b1, b2, 0]
print(f"\nVector b: {b}\n")

x = np.linalg.solve(matrix, b)

formatted = [f"{value:.8f}" if value != 0 else "0" for value in x]
print("Vector x: [" + " ".join(formatted) + "]")








