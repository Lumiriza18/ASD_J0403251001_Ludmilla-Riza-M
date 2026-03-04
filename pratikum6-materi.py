#======================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#=============================================

#=====================================
#insertion sort(ascending)
#=====================================
def insertion_sort(data):
    #loop mulai dari data ke-2(index arry ke 1)
    for i in range(1,len(data)):

        key = data[i] #simpan nilai yang disisipkan
        j = i-1 #indexelemendi baginan kiri

#geser
        while j>=0 and data[j] > key:
            data[j+1]=data[j]
            j-=1
        #sisipkan key ke posisis yang bener
        data[j+1]=key
    return data

angka=[7,8,5,2,4,6]
print("hasil shorting ->", insertion_sort(angka))


