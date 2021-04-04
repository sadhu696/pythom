n = int(input())
res = [[0 for i in range(n)] for j in range(n)]
i = 0
#stp - переменная шаг, которая уменьшается на 2 каждые две итерации
stp = 0
#cnt - переменная-счетчик итераций
cnt = 0
#cntd - счетчик прохода матрицы по кругу
cntd = 0
#k - переменная счетчик от 1 до n
k = 1
#общий цикл для заполнения всей матрицы.
while i < (n*2-1):
    #цикл для заполнения строки слева направо
    for j in range(n-stp):
        res[cntd][j+cntd] = k
        k += 1
    stp += 1
    i += 1
    #цикл для заполнения столбцов сверху вниз
    for j in range(n-stp):
        res[j+cntd+1][n-cntd-1] = k
        k += 1
    i += 1
    #цикл для заполнения строки справа налево
    for j in reversed(range(n-stp)):
        res[n-cntd-1][j+cntd] = k
        k += 1
    stp += 1
    i += 1
    #цикл для заполнения столбца снизу вверх
    for j in reversed(range(n-stp)):
        res[j+1+cntd][cntd] = k
        k += 1
    i += 1
    cntd += 1
#цикл для вывода итоговой матрицы
for i in range(n):
    for j in range(n):
        print(res[i][j], end=" ")
    print()

