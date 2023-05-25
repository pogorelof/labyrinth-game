import random


def maze_generator(size):
    maze = [['#' for _ in range(size)] for _ in range(size)]

    #СОЗДАНИЕ ИСТИННОГО ПУТИ

    #конец
    space_index = [random.randint(0, size-1)]
    maze[0][space_index[0]] = '*'

    for i, sym in enumerate(maze):
        if i == 0 or i == size - 1:
            continue

        #лабиринт пойдет влево или право: False - лево, True - право
        left_or_right = random.choice([True, False])
        #на сколько клеток
        if left_or_right:
            maximum = len(maze) - space_index[len(space_index)-1] - 1
            if maximum == 0:
                left_or_right = not left_or_right
            spaces = random.randint(1, maximum)
        if not left_or_right:
            maximum = space_index[0]
            if maximum == 0:
                left_or_right = not left_or_right
                maximum = 2
            spaces = random.randint(1, maximum)
        #заполнение
        if left_or_right:
            j = space_index[len(space_index)-1]
            space_index.clear()
            for _ in range(spaces):
                maze[i][j] = ' '
                space_index.append(j)
                j += 1
        if not left_or_right:
            j = space_index[0]
            space_index.clear()
            for _ in range(spaces):
                maze[i][j] = ' '
                space_index.append(j)
                j -= 1
    
    #начало
    try:
        end_index = random.randint(space_index[0], space_index[len(space_index)-1])
    except:
        end_index = space_index[0]
    maze[size-1][end_index] = 'P'

    #СОЗДАНИЕ НЕВЕРНЫХ ПУТЕЙ
    row_min = 1
    row_max = size - 2
    column_min = 1
    column_max = size - 2

    #частота неверных путей
    #чем больше значение, тем меньше неверных путей
    frequence = 1

    count = random.randint(2, size**2/frequence)

    for i in range(count):
        random_row = random.randint(row_min, row_max)
        random_column = random.randint(column_min, column_max)
        maze[random_row][random_column] = ' '

    return maze


# size = 22
#
# maze = maze_generator(size)
#
# for i, line in enumerate(maze):
#     print(f'{i} - {line}')