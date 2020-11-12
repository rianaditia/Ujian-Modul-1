def create_phone_number(number):

    """ Fungsi yang akan mengolah 10 digit integer menjadi sebuah nomor telepon """

    return f"({number[0]}{number[1]}{number[2]}) {number[3]}{number[4]}{number[5]}-{number[6]}{number[7]}{number[8]}{number[9]}"
    # Mencetak langsung nomor telepon dengan metode formatting


print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))