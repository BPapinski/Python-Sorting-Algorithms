def MergeSort(array_to_sort):
    global extra_array  # deklarujemy globalną tablicę pomocniczą
    extra_array = [0] * len(array_to_sort)  # tworzymy dodatkową tablicę
    merge_sort_function(array_to_sort, 0, len(array_to_sort) - 1)  # sortujemy zadaną tablicę


def merge_sort_function(array, left_index, right_index):
    if left_index < right_index:  # sprawdzamy, czy mamy więcej niż jeden element
        pivot = (left_index + right_index) // 2
        merge_sort_function(array, left_index, pivot)  # sortujemy lewą stronę
        merge_sort_function(array, pivot + 1, right_index)  # sortujemy prawą stronę
        merge(array, left_index, pivot, right_index)  # łączymy lewą, prawą i pivot


def merge(array, left_index, pivot, right_index):
    # zapisujemy wartości początkowe
    for i in range(left_index, right_index + 1):
        extra_array[i] = array[i]

    finger1 = left_index  # wskazuje na element z lewej części tablicy
    finger2 = pivot + 1  # wskazuje na element z prawej części tablicy
    current = left_index

    # porównujemy elementy z obu części
    while finger1 <= pivot and finger2 <= right_index:
        if extra_array[finger1] <= extra_array[finger2]:  # jeśli po lewej jest mniejszy
            array[current] = extra_array[finger1]  # przepisujemy do tablicy wynikowej
            finger1 += 1
        else:
            array[current] = extra_array[finger2]  # przepisujemy mniejszy z prawej
            finger2 += 1
        current += 1

    # jeśli zostały jakieś elementy po lewej stronie, przepisujemy je
    while finger1 <= pivot:
        array[current] = extra_array[finger1]
        current += 1
        finger1 += 1


# wersja z zajec

def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr) // 2

        l = arr[0:m]
        r = arr[m:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1