import math


# arr = [0.8, 0.399, 0.45, 0.7, 0.55, 0.003, 0.15, 0.999, 0.5, 0.666, 0.3, 0.1, 0.2, 0.79, 0.7, 0.8]

#   bucket #0 -> [0.0, 0.2) -> 0.1, 0.15, 0.03
#   bucket #1 -> [0.2, 0.4) -> 0.399, 0.2, 0.3
#   bucket #2 -> [0.4, 0.6) -> 0.5, 0.55, 0.45
#   bucket #3 -> [0.6, 0.8) -> 0.7, 0.79, 0.666, 0.7
#   bucket #4 -> [0.8, 1.0) -> 0.8, 0.999, 0.87, 0.8


# sortuje kazy kubelek - insertion sort czy cos

#   bucket #0 -> [0.0, 0.2) -> 0.03,  0.1, 0.15
#   bucket #1 -> [0.2, 0.4) ->  0.2, 0.3, 0.399,
#   bucket #2 -> [0.4, 0.6) ->  0.45, 0.5, 0.55
#   bucket #3 -> [0.6, 0.8) ->  0.666, 0.7, 0.7, 0.79,
#   bucket #4 -> [0.8, 1.0) -> 0.8, 0.8, 0.87,  0.999


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


def BucketSort(arr, noOfbuckets):
    if len(arr) == 0:
        return arr

    max_ele = max(arr)
    min_ele = min(arr)

    noOfbuckets = int(math.ceil(len(arr) ** (1 / 2)))  # pierwiastek z liczb =y elementow ceiling

    rnge = (max_ele - min_ele) / noOfbuckets if max_ele != min_ele else 1

    temp = []

    for i in range(noOfbuckets):
        temp.append([])

    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)

        if diff == 0 and arr[i] != min_ele:
            temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])
        else:
            temp[int((arr[i] - min_ele) / rnge)].append(arr[i])

    for i in range(noOfbuckets):
        quickSort(temp[i], 0, len(temp[i]) - 1)

    k = 0

    for i in range(noOfbuckets):
        for j in range(len(temp[i])):
            arr[k] = temp[i][j]
            k += 1
    return arr


arr = [0.8, 0.399, 0.45, 0.7, 0.55, 0.003, 0.15, 0.999, 0.5, 0.666, 0.3, 0.1, 0.2, 0.79, 0.7, 0.8]

print("posortowana: ")
# print(BucketSort(arr))


# rnge = (max - min)/n

# bucketIndex = (arr[i] )


arr = [9.8, 0.6, 10.1, 1., 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
noOfbuckets = int(math.ceil(len(arr) ** (1 / 2)))

# bucket #0 -> 0.6, 1.9

# bucket #1 -> 3,04, 3.07

# bucket #2 -> 5.0, 4.8

# bucket #3 > 8.0, 7.68

# arr = [0.6, 1.9, 3.04, 3.07, 4.8, ...]


print(BucketSort(arr, noOfbuckets))
# bucket #4 -> 9.8, 10.1