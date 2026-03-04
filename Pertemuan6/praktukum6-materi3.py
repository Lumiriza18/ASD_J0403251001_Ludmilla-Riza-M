#======================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#=============================================

#=====================================
#insertion dengan traction
#=====================================
def merger_sord(data,depth):
    indent=" "*depth
    print(f"{indent}marger_sord({data})")

    if len(data) <= 1:
        return data

    #divide : membagi data menjadi 2 bagian
    mid=len(data)//2
    left= data[:mid] #slicing bagian kiri
    right=data[mid:] #slicing bagian kanan

    print(f"{indent}divide-> left={left}|right={ right}")

#8 ==> left 4 right 4
#left 4 ==> mengesort ==>


# #recursive call
    left_sorted=merger_sord(left)
    right_sorted=merger_sord(right)
    return merge(left_sorted,right_sorted)

def merge(left,right):
    result=[]
    i=0
    j=0

    #membandingkan elemen kiridan kanan
    while i < len(left) and len(right):
        if left[i] <= right[i]:
            result.append(left[j])
            i+=1
        else:
            result.append(right[j])
            j+=1
    #menambahkan sisa elemen jika ada
    result.extend(right[i:])
    result.extend(left[j:])

angka=[13,7,28,5,19,36,4]
print("hasil sorting:", merger_sord(angka))
    




