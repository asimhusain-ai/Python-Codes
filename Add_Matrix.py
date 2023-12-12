def add_matrix(m1, m2):
    result = [[m1[i][j] + m2[i][j]
    for j in range(len(m1[0]))]
    for i in range(len(m1))]
    return result
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
    ]
result_matrix = add_matrix(m1, m2)
for row in result_matrix:
    print(row)
