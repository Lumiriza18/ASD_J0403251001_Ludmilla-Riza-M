#===================================================
#nama: Ludmilla Riza Maharuni
#nim: J0403251001

#==================================================
#kita tambah parameter 'depth' biar bisa bikin indentasi otomatis 
def merge_sort(data, depth=0):
    indent = " " *depth #membuat spasi sesuai kedalaman rekursi 
    print(f"{indent}---> masuk merge_sort({data})")
    
    #base case: kalau data cuma 1, langsung balik badan 
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    print(f"{indent}  divide: {left} dan {right}")

    #recursive call: panggil lagi sambil nambah depthnya
    left_sorted = merge_sort(left, depth + 1)
    right_sorted = merge_sort(right, depth + 1)

    #conquer : gabungin lagi 
    merged = merge(left_sorted, right_sorted)
    print(f"{indent}  merge:{left_sorted} + {right_sorted} => {merged}")

    return merged

def merge(left,right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            i += 1
        else: 
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

#data uji 
angka = [13,7,28,5,19,26,4]
print("==== program tracing merge sort ====")
hasil = merge_sort(angka)
print("\n===== HASIL AKHIR =====")
print("data awal  :", angka)
print("hasil sorting:", hasil)