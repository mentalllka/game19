def check(l1, c1, l2, c2):  # проверка корректности введенных координат
    if l1 == l2 and c1 == c2:  # координаты не должны совпадать
        return 0
    if gf[l1][c1] == '-' or gf[l2][c2] == '-':  # в ячейке не должно быть '-'
        return 0
    if gf[l1][c1] + gf[l2][c2] == 10:  # числа можно убрать, если их сумма 10
        return 1
    if gf[l1][c1] == gf[l2][c2]:  # если числа равны
        if c1 == c2:  # если находятся в одном столбце
            return 1 if all(gf[l1][c] == '-' for c in range(min(c1, c2) + 1, max(c1, c2))) else 0
        if l1 == l2:  # если находятся на одной линии
            return 1 if abs(c1 - c2) == 1 or (gf[l1][min(c1, c2) + 1:max(c1, c2)] == ['-'] * (abs(c1 - c2) - 1)) else 0
    return 0

def finish(gf):  # проверка возможности найти ячейки для взаимодействия
    if gf.count('-') == 26:
        return 0
    for l1 in range(3):
        for c1 in range(9):
            for l2 in range(3):
                for c2 in range(9):
                    if check(l1, c1, l2, c2) == 1:
                        return 1
    return 0

def finalgamefield(gf):  # отрисовка финального поля
    if gf.count('-') == 26 and gf[2][8] == '9':
        return gf

    lastcell = 0
    for l1 in range(3):
        for c1 in range(9):
            if gf[2 - l1][8 - c1] != '-':
                gf[2 - (lastcell // 9)][8 - lastcell] = gf[2 - l1][8 - c1]
                gf[2 - l1][8 - c1] = '-'
                lastcell += 1
    return gf

gf = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
      [1, 1, 1, 2, 1, 3, 1, 4, 1],
      [5, 1, 6, 1, 7, 1, 8, 1, 9]]

gameover = 0
while gameover == 0:
    if finish(gf) == 1:
        print('   1 2 3 4 5 6 7 8 9')
        print(' -------------------')
        for i, row in enumerate(gf):
            print(f'{i + 1}| ' + ' '.join(map(str, row)))

        l1, c1 = int(input('Введите номер линии первого элемента: ')) - 1, int(input('Введите номер столбца первого элемента: ')) - 1
        l2, c2 = int(input('Введите номер линии второго элемента: ')) - 1, int(input('Введите номер столбца второго элемента: ')) - 1

        if check(l1, c1, l2, c2) == 1:
            gf[l1][c1], gf[l2][c2] = '-', '-'
        else:
            print('Координаты введены некорректно')
    else:
        print('Игра окончена!')
        gameover = 1
        fgf = finalgamefield(gf)
        for row in fgf:
            print(*row)
