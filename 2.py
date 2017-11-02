
matrix = [[0.5, 0, 0, 0, 0],
          [1, 0.5, 0, 0, 0],
          [1, 1, 0.5, 0, 0],
          [1, 1, 1, 0.5, 0],
          [1, 1, 1, 1, 0.5]]

matrix_t = list(zip(*matrix))	# - 

#print(matrix)
#print(matrix_t)

for line in matrix:
    print(line)
    print(sum(line))
print('\n')
for line in matrix_t:
    print(list(line))	# - явное преобразование типов

print('*' * 25)
