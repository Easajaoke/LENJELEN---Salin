data = [1,2,3,3,4,5,6,7,7]
left = 0
right = len(data)-1
Dataditemukan = False
Cari = 3
while left < right:
    middle = (left + right)//2
    if data[middle] == Cari:
        left = middle + 1
        middle2 = (left + right)//2
        Dataditemukan = True
    else:
        if Cari < data[middle]:
            right = middle - 1
        else:
            left = middle + 1
if Dataditemukan:
    if left == right:
        print("Data ditemukan pada index ke- ", (middle + 1))
    else:
        print("Data ditemukan pada index ke- ", (middle))
else:
    print("Data tidak ditemukan")
