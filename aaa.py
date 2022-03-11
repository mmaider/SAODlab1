import random


def tournamentSort(matrix):
    tree = [None] * 2 * (len(matrix) + len(matrix) % 2)
    index = len(tree) - len(matrix) - len(matrix) % 2

    for i, v in enumerate(matrix):
        tree[index + i] = (i, v)

    for j in range(len(matrix)):
        n = len(matrix)
        index = len(tree) - len(matrix) - len(matrix) % 2
        while index > -1:
            n = (n + 1) // 2
            for i in range(n):
                i = max(index + i * 2, 1)
                if tree[i] != None and tree[i + 1] != None:
                    if tree[i][1] < tree[i + 1][1]:
                        tree[i // 2] = tree[i]
                    else:
                        tree[i // 2] = tree[i + 1]
                else:
                    tree[i // 2] = tree[i] if tree[i] != None else tree[i + 1]
            index -= n
        index, x = tree[0]
        matrix[j] = x
        tree[len(tree) - len(matrix) - len(matrix) % 2 + index] = None

def TournamentSort(matrix):
    for i in range(len(matrix)):
        tournamentSort(matrix[i])
    return matrix


a = []
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(random.randint(1, 99))
test = a.copy()
print('Исходный массив: ' + str(test))
print('Сортировка: ' + str(test))
