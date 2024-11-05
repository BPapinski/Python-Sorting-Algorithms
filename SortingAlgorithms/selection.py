def SelectionSort(array):
    for i in range(len(array) - 1):
        index = i  # index najmniejszego elementu
        for j in range(i + 1, len(array)):
            if array[j] < array[index]:
                index = j

        # zamiana elementów miejscami
        array[i], array[index] = array[index], array[i]
