#======================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#=============================================

#=====================================
#insertion sort tracing
#=====================================
def insertion_sort(data):

    print("data awal",data)
    print("="*50)

    #loop mulai dari data ke-2(index arry ke 1)
    for i in range(1,len(data)):

        
        key = data[i] #simpan nilai yang disisipkan
        j = i-1 #indexelemendi baginan kiri

        print("interasi ke-",i)
        print("nilai key ke", key)
        print("bagian kiri(terurut)", data[:1])
        print("bagian kanan (belum urut):",data[i:])

#geser
        while j>=0 and data[j] > key:
            data[j+1]=data[j]
            j-=1
        #sisipkan key ke posisis yang bener
        data[j+1]=key

        print("setelah disisipkan",data)
        print("-"*50)
    return data

angka=[7,8,5,2,4,6]
print("hasil shorting ->", insertion_sort(angka))


