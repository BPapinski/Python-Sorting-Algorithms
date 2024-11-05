def BubbleSort(T):
    N = len(T)
    for i in range(0, N):
        for j in range(0, N-1-i): # sortuje od pierwszego elementu do elementu ktory stanowi bariere posortowanej i nieposortowanej czesci tablicy
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
