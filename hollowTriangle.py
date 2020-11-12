def hollowTriangle(t):

    """ Fungsi yang akan mencetak setigiga hollow dengan memasukkan tinggi (jumlah baris) yang dikehendaki"""

    for i in range(t): # Menentukan jumlah baris yang akan dicetak
        
        for j in range((t*2)-1): # Menentukan jumlah kolom yang akan dicetak
            if i == t-1 or i+j == t-1 or j-i == t-1: # Hanya mencetak '#' pada 3 kondisi tersebut
                print('# ', end = '')
            else:
                print('__', end = '') # Mencetak '_' pada kondisi di luar 3 kondisi tersebut
        print()

hollowTriangle(8)
            