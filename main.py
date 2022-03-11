from random import randint


# сортировка выбором
def vibor(arr):
    m, n = len(arr), len(arr[0])
    newarr = sum(arr, [])
    for i in range(len(newarr) - 1):
        a = i
        b = i + 1
        while b < len(newarr):
            if newarr[b] < newarr[a]:
                a = b
            b = b + 1
        newarr[i], newarr[a] = newarr[a], newarr[i]
    counter = 0
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(newarr[counter])
            counter += 1
        arr[i] = temp


# сортировка вставкой
def vstavka(arr):
    m, n = len(arr), len(arr[0])
    newarr = sum(arr, [])
    for i in range(1, len(newarr)):
        a = newarr[i]
        b = i - 1
        while b >= 0 and a < newarr[b]:
            newarr[b + 1] = newarr[b]
            b -= 1
        newarr[b + 1] = a
    counter = 0
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(newarr[counter])
            counter += 1
        arr[i] = temp


# сортировка обменом(пузырьком)
def obmen(arr):
    m, n = len(arr), len(arr[0])
    newarr = sum(arr, [])
    length = len(newarr)
    for i in range(length):
        for j in range(0, length - i - 1):
            if newarr[j] > newarr[j + 1]:
                newarr[j], newarr[j + 1] = newarr[j + 1], newarr[j]
    counter = 0
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(newarr[counter])
            counter += 1
        arr[i] = temp


# сортировка Шелла
def shell(arr):
    m, n = len(arr), len(arr[0])
    newarr = sum(arr, [])
    length = len(newarr)
    gap = length // 2
    while gap > 0:
        for iIndex in range(gap, length):
            temp = newarr[iIndex]
            jIndex = iIndex
            while jIndex >= gap and newarr[jIndex - gap] > temp:
                newarr[jIndex] = newarr[jIndex - gap]
                jIndex -= gap
            newarr[jIndex] = temp
        gap //= 2
    counter = 0
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(newarr[counter])
            counter += 1
        arr[i] = temp


# Турнирная сортировка
def tournament(arr):
    m, n = len(arr), len(arr[0])
    newarr = sum(arr, [])
    tree = [None] * 2 * (len(newarr) + len(newarr) % 2)
    index = len(tree) - len(newarr) - len(newarr) % 2

    for i, v in enumerate(newarr):
        tree[index + i] = (i, v)

    for j in range(len(newarr)):
        n = len(newarr)
        index = len(tree) - len(newarr) - len(newarr) % 2
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
        newarr[j] = x
        tree[len(tree) - len(newarr) - len(newarr) % 2 + index] = None
    counter = 0
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(newarr[counter])
            counter += 1
        arr[i] = temp


# Пирамидальная сортировка
# вспомогательная функция расчётов
def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


# функция перестановки
def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


a = []
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(randint(1, 99))
test = a.copy()
print('Исходный массив: ' + str(test))
vibor(test)
print('Сортировка выбором: ' + str(test))
test = a.copy()
vstavka(test)
print('Сортировка вставкой: ' + str(test))
test = a.copy()
obmen(test)
print('Сортировка обменом: ' + str(test))
test = a.copy()
shell(test)
print('Сортировка Шелла: ' + str(test))
test = a.copy()
tournament(test)
print('Турнирная сортировка: ' + str(test))
test = a.copy()
heap_sort(test)
print('Пирамидальная сортировка: ' + str(test))
