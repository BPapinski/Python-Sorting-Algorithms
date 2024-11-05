def ShellSort(T):
    swap_counter = 0
    gap = len(T) // 2

    while gap > 0:  # ogólny warunek
        j = gap
        while j < len(T):  # patrzymy, czy j (element z porównywanej pary na prawo) nie wyjechał poza tablicę
            i = j - gap  # wyznaczamy indeks elementu po lewej z porównywanej pary
            while i >= 0:
                if T[i + gap] > T[i]:  # sprawdzamy, czy są dobrze posortowane
                    break
                if T[i + gap] <= T[i]:  # jeśli są źle, zamieniamy miejscami
                    T[i + gap], T[i] = T[i], T[i + gap]
                    swap_counter += 1
                i -= gap  # przesuwamy lewą granicę o gap w lewo, aby zmienić element porównywany po lewej
            j += 1  # zwiększamy indeks elementu porównywanego po prawej o 1
        gap //= 2  # zmniejszamy gap o połowę

    return swap_counter  # zwracamy liczbę zamian

def LazarusShellSort(arr, n):
    swapCounter = 0
    gap = 2 * (n // (pow(2, 1) )) + 1

    while(gap > 0):
        j = gap
        while j < len(arr):
            i = j - gap
            while i>=0:
                if arr[i+gap] > arr[i]:
                    break
                if arr[i+gap] <= arr[i]:
                    arr[i+gap], arr[i] = arr[i], arr[i+gap]
                    swapCounter += 1
                i -= gap
            j += 1
        if gap == 1:
            break
        gap = 2 * (n // (pow(2, j + 1))) + 1
    print("LazarusShellSort swap counter: ", swapCounter)