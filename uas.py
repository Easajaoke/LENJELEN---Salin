import csv #mentransfer data csv ke python
NIM = []
Name = []
with open('DaftarNama.csv') as csv_file: #dengan membuka file csv
        csv_reader = csv.reader(csv_file, delimiter = ';')
        line_count = 0
        for row in csv_reader: 
                NIM.append(row[0])
                Name.append(row[1])

def AllData(): #fitur untuk menampilkan seluruh data
    for row in range(len(Name)): #looping untuk mencari data sebanyak data dalam array
        print(NIM[row],Name[row]) #mencetak NIM dan nama sesuai looping
    print("") #memberi satu jarak baris kosong

def AddData(): #fitur untuk menambahkan data baru
    with open('DaftarNama.csv', mode='a')as csv_file: #dengan membuka file csv
        csv_writer = csv.writer(csv_file, delimiter = ';')
        jumlah = int(input("How much data will be added? "))
        for a in range(jumlah): #looping sesuai inputan jumlah data yang akan ditambahkan
            NIMnew= str(input("NIM: ")) #menginputkan NIM baru
            NIM.append(NIMnew) #menambahkan NIM baru ke array NIM
            NameNew = " " + str(input("Name: ")) #menginputkan nama baru
            Name.append(NameNew) #menambahkan nama baru ke array nama
            csv_writer.writerow([NIMnew, NameNew])
    print('Saved!') #cetak 'Tersimpan!'
    print("") #memberi satu jarak baris kosong
    
def SearchData(): #fitur untuk menampilkan pencarian data
    SearchData = str(input("Insert Name or NIM: ")) # variable untuk menampung nama atau NIM yang akan dicari
    with open ('DaftarNama.csv') as csv_file : #dengan membuka file csv
        reader = csv.reader(csv_file,delimiter = ";") 
        print ()
        for Data in reader :  #perulangan dalam data reader
            left = 0 #left merupakan variable yang menentukan batas kiri yang dimulai dari 0
            right = len(Data)-1 #right merupakan variabel yang menentukan batas kanan yang banyak datanya sama dengan panjang data
            while left <= right: #memulai perulangan dengan mengecek
                mid = (left + right)//2 #mendeklarasikan variable mid dengan mengoprasikan left dan right
                if SearchData != Data[mid]: #mengecek nilai SearchData apakah tidak sama dengan 
                    if Data[mid] < SearchData:
                        left = mid + 1
                    else:
                        right = mid - 1
            try: 
                if SearchData in Data[0]: 
                    print("Name:", Data[1])
                    print("NIM:", Data[0])
                    print()
                if SearchData in Data[1].lower():
                    print("Name:", Data[1])
                    print("NIM:", Data[0])
                    print()
            except:pass
    print("") #memberi satu jarak baris kosong
            
def DeleteData(): #fitur untuk menghapus data
    DeleteData = input('Insert NIM / Name will delete: ')
    if DeleteData in NIM: #jika inputan NIM ada di data NIM
        index_NIM = NIM.index(DeleteData) #mencari tahu di mana index NIM
        print('Succes Deleted') #mencetak untuk memberi tahu bahwa data berhasil dihapus
        NIM.remove(NIM[index_NIM]) #menghapus NIM sesuai index NIM
        Name.remove(Name[index_NIM]) #menghapus nama sesuai index NIM
        with open ('DaftarNama.csv','w',newline="") as csv_file: #dengan membuka file csv
            csv_writer = csv.writer(csv_file,delimiter=';') #menambahkan row ke file .csv dan menampung ke var csv_file
            for nom,er in zip (NIM,Name): 
                csv_writer.writerow([nom]+[er])
        csv_file.close()
    elif DeleteData in Name: #jika inputan nama ada di data nama
        index_Name = Name.index(DeleteData) #mencari tahu di mana index nama
        print('Succes Deleted') #mencetak untuk memberi tahu bahwa data berhasil dihapus
        NIM.remove(NIM[index_Name]) #menghapus NIM sesuai index nama
        Name.remove(nama[index_Name]) #menghapus nama sesuai index nama
        with open ('DaftarNama.csv','w',newline="") as csv_file: #dengan membuka file csv
            csv_writer = csv.writer(csv_file,delimiter=';') #menambahkan row ke file .csv dan menampung ke var csv_file
            for nom,er in zip(NIM,Name):
                csv_writer.writerow([nom]+[er])
        csv_file.close()
    else: #selain kedua pilihan tersebut
        print('Not Found!') #mencetak untuk memberi tahu bahwa data tidak ditemukan
    print("") #memberi satu jarak baris kosong
    
def NIMDesc(): #fitur untuk deklarasi nama fungsi sorting
    max = len(NIM) #deklarasi nama variable max yang nilainya sama dengan panjang data nim
    for a in range(max-1,0,-1): #looping untuk menentukan banyak proses yang akan dilakukan saat pengurutan
        for b in range(a): #melakukan perulangan dengan variable b sebanyak a untuk mengurutkan nilai yang ada
            if NIM[b] > NIM[b + 1]: #jika NIM pada index sebelumnya lebih besar daripada index setelahnya akan berlaku oprasi di bawahnya
                c = NIM[b + 1] #NIM pada index setelahnya terlebih dahulu ditampung di variable c
                d = Name[b + 1] #nama pada index yang sama dengan NIM terlebih dahulu ditampung di variable d
                NIM[b + 1] = NIM[b] #karena NIM[b + 1] kosong maka diisi oleh nilai index sebelumnya
                Name[b + 1] = Name[b] #karena nama[b + 1] kosong maka diisi oleh nilai index sebelumnya
                NIM[b] = c #NIM yang ada pada variable c dipindahkan ke variable NIM[b]
                Name[b] = d #nama yang ada pada variable d dipindahkan ke variable nama[b]
    for row in NIM : #looping untuk mengubah tampilan menjadi list
        index = NIM.index(row) #looping untuk mencari data sebanyak data dalam array           
        print(row,end = '') #untuk memberi ruang kosong
        print(Name[index]) # menampilkan nama sesuai index
    print("") #memberi satu jarak baris kosong
     
while True: #perulangan untuk mengetikkan menu
        menu = input('All Data\nAdd Data\nSearch Data\nDelete Data\nSorting\nWrite the menu: ')   
        if menu == 'All Data':
            AllData()
        elif menu == 'Add Data':
            AddData()
        elif menu == 'Search Data':
            SearchData()
        elif menu == 'Delete Data':
            DeleteData()
        elif menu == 'Sorting':
            NIMDesc()
        elif menu == 'Close':
            exit()
