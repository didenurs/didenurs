# matrix açılımı
listA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listB = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

name1 = "MatrixA"
name2 = "MatrixB"

def PrintMatrix(row_count, column_count,list_matrix, name_matrix):
    i = 0
    for row in range(row_count):
        for col in range(column_count):
            print(list_matrix[i], end='')
            i += 1
        print('')
    print(str(name_matrix))

PrintMatrix(3,3,listA,name1)
PrintMatrix(5,3,listB, name2)
