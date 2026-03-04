#=============================================
# Nama: Ludmilla Riza Maharuni
# NIM: J0403251001
#latihan 3
#=============================================

def insertion_sort(data):
    for i in range(1,len(data)):
        key = data[i]
        j=i-1
        while j>=0 and data[j] > key:
            data[j+1]=data[j]
            j-=1
        data[j+1] = key
        return data
data=[5,2,4,6,1,3]
sorted_data=insertion_sort(data)
print("hasil akhir:", sorted_data)

'''
1. isi list setelah iterasi i=1:
i=1 mengambil angka 2(key),karena 5>2 maka angka 5 bergeser ke kanan
dan angka 2 diletakkan di depan
[2,5,4,6,1,3]

2. isi lidt setelah iterasi i=3
list awal = [5,2,4,6,1,3]
iterasi i = 1 :[2,5,4,6,1,3]
iterasi i= 2 :[2,4,5,6,1,3]
iterasi i = 3 :[2,4,5,6,1,3] tidak berubah karena 6 >dari 5

3. pergeseran terjadi pada iterasi i = 4 adalah sebanyak 4 kali pergeseran 
'''
