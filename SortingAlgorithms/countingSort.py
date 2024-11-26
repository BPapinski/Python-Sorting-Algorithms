def countingSort(array):
    _max = max(array) # maksymalny element
    count = [0]*(_max+1) # przygotuwujemy tablice do zliczania ilosci wystapien elementow
    for element in array: # zliczamy
        count[element] += 1
    output = []
    for i in range (0, len(count)): # umieszczamy zliczone elementy w dobrej kolejnosci w tablicy wyjsciowej
        for j in range(0, count[i]):
            output.append(i)
    print(output)


arr = [1, 3,3, 7, 5, 2, 5, 5, 2, 5, 6, 7, 7, 3, 4, 2]

countingSort(arr)