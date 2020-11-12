def sort_odd_even(num):


    ''' Fungsi yang akan mengurutkan sebuah list berisi angka, bilangan genap diurutkan secara descending, 
        dan bilangan ganjil secara ascending. '''

    # Mempersiapkan container untuk menampung hasil pemisahan antara bilangan ganjil dan genap
    list_genap = [] 
    list_index_genap = []

    list_ganjil = []
    list_index_ganjil = []

    for i in range(len(num)):  # Memisahka bilangan ganjil dan genap dengan looping

        if num[i] % 2 == 0: # Memisahkan bilangan genap ke dalam list yang sudah dipersiapkan
            list_genap.append(num[i])
            list_index_genap.append(i)
            

        elif num[i] % 2 != 0:   # Memisahkan bilangan ganjil ke dalam list yang sudah dipersiapkan
            list_ganjil.append(num[i])
            list_index_ganjil.append(i)
            
    
    list_genap.sort(reverse = True) # Mengurutkan bilangan genap secara descending
    list_ganjil.sort()  # Mengurutkan bilangan ganjil secara ascending

    # Mengganti element yang ada di dalam list num dengan bilangan ganjil-genap yang sudah diurutkan
    for i in range(len(list_genap)):   # Memasukkan element bilangan genap dengan indeks yang sudah sesuai
        num[list_index_genap[i]] = list_genap[i]

    for i in range(len(list_ganjil)):   # Memasukkan element  bilangan ganjil dengan indeks yang sudah sesuai
        num[list_index_ganjil[i]] = list_ganjil[i]

    return num

print(sort_odd_even([3,5,2,8,1,4]))
