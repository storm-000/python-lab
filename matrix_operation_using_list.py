print("Matrix Operations on Two Matrices")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter Matrix A:")
A = []
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

print("\nEnter Matrix B:")
B = []
for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

add = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    add.append(row)

sub = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] - B[i][j])
    sub.append(row)

mul = []
for i in range(rows):
    row = []
    for j in range(cols):
        total = 0
        for k in range(cols):
            total += A[i][k] * B[k][j]
        row.append(total)
    mul.append(row)

transpose_A = []
for i in range(cols):
    row = []
    for j in range(rows):
        row.append(A[j][i])
    transpose_A.append(row)

transpose_B = []
for i in range(cols):
    row = []
    for j in range(rows):
        row.append(B[j][i])
    transpose_B.append(row)

print("\nMatrix A + B =")
print(add)

print("\nMatrix A - B =")
print(sub)

print("\nMatrix A × B =")
print(mul)

print("\nTranspose of Matrix A =")
print(transpose_A)

print("\nTranspose of Matrix B =")
print(transpose_B)
