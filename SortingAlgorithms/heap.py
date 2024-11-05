import datetime
import random
import time

def heapify(arr, n, i):  # max heap --- i - wezel ktory "kopcujemy"
    largest = i # zakladamy ze wezel jest najwiekszy
    l = 2 * i + 1 # lewy syn
    r = 2 * i + 2 # prawy syn

    if l < n and arr[largest] < arr[l]: # sprwadzamy czy element po lewo istnieje i jesli tak to czy jest wiekszy od najwiekszego elementu
        largest = l # jesli tak to jest najwiekszy
    if r < n and arr[largest] < arr[r]: # sprwadzamy czy element po prawo istnieje i jesli tak to czy jest wiekszy od najwiekszego elementu
        largest = r # jesli tak to jest najwiekszy

    if largest != i: # jesli ktorys z synów jest wiekszy
        arr[i], arr[largest] = arr[largest], arr[i] # zamieniamy go z ojcem

        heapify(arr, n, largest) # kopcujemy wezel z ktorego "zabralismy" wiekszy element aby upewnic sie ze struktura kopca jest zachowana na nizszych poziomach


def heapify2(arr, n, i):  # min heap
    lowest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[lowest] > arr[l]:
        lowest = l
    if r < n and arr[lowest] > arr[r]:
        lowest = r

    if lowest != i:
        arr[i], arr[lowest] = arr[lowest], arr[i]

        heapify2(arr, n, lowest)


def heapsort(arr):
    n = len(arr)

    #budowanie kopca
    for i in range(n // 2, -1, -1): # iterujemy przez elementy od polowy do ojca, od polowy dlatego aby nie robic heapify na najnizszym poziomie bo wiadomo ze nie maja dzieci
        heapify(arr, n, i)


    #mamy tablice jako kopiec - mozna sortować
    for i in range(n - 1, 0, -1): # przechodzimy od najnizych poziomów do najwyższych
        arr[i], arr[0] = arr[0], arr[i] # przenosimy analizowany element na gore kopca
        heapify(arr, i, 0) # sortujemy analizowana galez




def ternary_heapify(arr, n, i): # sortowanie przez kopcowanie ale kazdy ojciec bedzie mial troje dzieci
    largest = i # ojciec
    left = 3 * i + 1 # lewe dziecko
    middle = 3 * i + 2 # srodkowe dziecko
    right = 3 * i + 3 # prawe dziecko

    if left < n and arr[left] > arr[largest]:
        largest = left

    if middle < n and arr[middle] > arr[largest]:
        largest = middle

    if right < n and arr[right] > arr[largest]:
        largest = right

    # w trzech ifach na górze szykalismy czy ktores dziecko jest starsze niz ojciec

    if largest != i: # jesli jest
        arr[i], arr[largest] = arr[largest], arr[i] # to wpierdalamy wieksze dziecko w miejsce starego
        ternary_heapify(arr, n, largest) # wywolujemy heapsort dla galezi z ktorej zabralismy element


def ternary_heap_sort(arr):
    n = len(arr)
    for i in range(n // 3 - 1, -1, -1): # przechodzimy przez elementy od 1/3 kopca w gore aby ominac najnizszy poziom
        ternary_heapify(arr, n, i) # kopcujemy
    # mamy już kopiec

    # to mozemy go teraz rozjebac w celu uzyskania posortowanej tablicy

    for i in range(n - 1, 0, -1): # przechodzimy przez caly kopiec od najnizszych warstw
        arr[i], arr[0] = arr[0], arr[i] # wrzucamy najwiekszy element (ojca) na ostatnie miejsce tablicy
        ternary_heapify(arr, i, 0)  # zmniejszony kopiec i sortujemy analizowana





def wypelnij(arr, n):
    for i in range(0, n, 1):
        arr.append(random.randint(-100, 100))


#N = input("wprowadz ilosc liczb w tablicy: ")
N = 10
arr = []

wypelnij(arr, N)

print(arr)

starttime = time.time()
ternary_heap_sort(arr)
endtime = time.time()

print(arr)

print('%.5f' % (endtime - starttime))

#print("{}".format(endtime - starttime))
