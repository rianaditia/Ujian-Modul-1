def Hashtag(string):


    ''' Fungsi yang akan menghasilkan hashtag dari string yang terpisah oleh spasi'''


    string_hashtag = '#'+string # Menambahkan # pada string yang dimasukkan
    string_title = string_hashtag.title()   # Mengubah huruf pertama setiap kata dari string yang dimasukkan
    list_string = string_title.split()  # Memisahkan setiap kata dan menjadikannya element di suatu list
    hasil_cetak = ''.join(list_string)  # Mencetak element - element yang ada di dalam list menjadi suatu kalimat tanpa spasi

    if (len(hasil_cetak) > 140) or (len(string) == 0) or (len(hasil_cetak) == 0): 
        # Syarat yang harus dipenuhi agar fungsi tidak mengembalikkan nilai False
        return False
    else:
        return hasil_cetak


print(Hashtag('     Hello     World   '))