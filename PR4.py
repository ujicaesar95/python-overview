#solve1
x = [40, 100, 1, 5, 25, 10]

def cobabubbleSort(x):
    for ini in range(len(x)-1,0,-1):
        for itu in range(ini):
            if x[itu] > x[itu+1]:
                tampung = x[itu]
                x[itu] = x[itu+1]
                x[itu+1] = tampung


cobabubbleSort(x)
print("urutannya adalah : " + str(x))


#solve2

x = [40, 100, 1, 5, 25, 10, ]

def cariMax(x):
    iMax = x[0]
    for i in range(1, len(x)):
       if(x[i] > iMax):
            iMax = x[i]

    return iMax

def cariMin(x):
    iMin = x[0]
    for i in range(1, len(x)):
       if(x[i] < iMin):
            iMin = x[i]

    return iMin

iMax = x[0]
for i in range(1, len(x)):
    if(x[i] > iMax):
        iMax = x[i]

iMin = x[0]
for i in range(1, len(x)):
    if(x[i] < iMin):
        iMin = x[i]

print("nilai terkecil = "+ str(iMin))
print("nilai terbesar = "+ str(iMax))

#versi 2

