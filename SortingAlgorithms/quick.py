def Partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def QuickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = Partition(arr, low, high)
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)


def QuickSort2(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = Partition(arr, low, high)
        if len(arr) - pi > len(arr)//2:
            QuickSort2(arr, low, pi-1)
            QuickSort2(arr, pi+1, high)
        else:
            QuickSort2(arr, pi+1, high)
            QuickSort2(arr, low, pi-1)