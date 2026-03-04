#=============================================
# Nama: Ludmilla Riza Maharuni
# NIM: J0403251001
#latihan 2
#=============================================
#<<<<<<<<<<<<<< sorting ascending<<<<<<<<<<<<<<<<<<
def insertion_sort(data):
    for i in range(1,len(data)):
        key= data[i]
        j=i-1

        while j >= 0 and data[j] > key :
            data[j+1]=data[j]
            j-=1
            data[j+1]=key
        return data
    
#>>>>>>>>>sorting  descending>>>>>>>>>>>>>>>>>>
    def insertion_sort(data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1

        # Ubah tanda '<' menjadi '>'
        while j >= 0 and key > data[j]: 
            data[j + 1] = data[j]
            j -= 1
            
        data[j + 1] = key
        
    return data