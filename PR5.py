#nomer 1
#search make filter

# list1 = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari ayam']
# search = input('search kata = ')

# def searchlist(keyword, list1):
#     newlist = list(filter(lambda item : keyword.lower() in item.lower(), list1))
#     return newlist

# hasilsearch = searchlist(search, list1)

# print(list1)
# print(hasilsearch)

#nomer 2 
#bikin fungsi map

#nomer 3
#bikin fungsi filter

#nomer 4
#Main Menu :
#1. Lihat menu
#2. Lihat cart
#3. Checkout
#4. Keluar

#1.
#1.Paket Bento A =  20000
#2.Paket Bento B =  25000
#3.Paket Bento C =  30000

#2.
#paket*Quantity

#3.
#total semuanya

#4. sampai jumpa lagi 

def menuutama(): 
    print("") 
    n = input('masukkan nama Konsumen: ') 
    print ('Nama Konsumen :'),n 
    print ("""Masukkan Pilihan 1. Bayar 2. Keluar""") 
    print("") 
def menuutama1(): 
    print ("""Masukkan Pilihan 1. Bayar 2. Keluar""") 
    print("") 

class makanan():     
    def bentoA (self,x): 
        jmlhpsn = x * 20000 
        pajak = jmlhpsn * 0.1 
        total = jmlhpsn + pajak 
        print ('Harga paket bento A = Rp 20.000') 
        print ('') 
        print ('Total Makanan = Rp '),jmlhpsn 
        print ('Pajak = Rp '),pajak 
        print ('___________________________________+') 
        print ('Total Seluruhnya = Rp '), total 
        return jmlhpsn 

    def bentoB (self,x): 
        jmlhpsn = x * 25000 
        pajak = jmlhpsn * 0.1 
        total = jmlhpsn + pajak 
        print ('Harga paket bento B = Rp 25.000') 
        print ('') 
        print ('Total Makanan = Rp '),jmlhpsn 
        print ('Pajak = Rp '),pajak 
        print ('___________________________________+') 
        print ('Total Seluruhnya = Rp '), total 
        return jmlhpsn

    def bentoC (self,x): 
        jmlhpsn = x * 30000 
        pajak = jmlhpsn * 0.1 
        total = jmlhpsn + pajak 
        print ('Harga paket bento C = Rp 30.000') 
        print ('') 
        print ('Total Makanan = Rp '),jmlhpsn 
        print ('Pajak = Rp '),pajak 
        print ('___________________________________+') 
        print ('Total Seluruhnya = Rp '), total 
        return jmlhpsn 


def back_menu(): 
    print ("Apakah anda ingin memesan lagi? [Y/N] :") 
    back = input().upper() 
    if back == 'Y': 
        menuutama1() 
        pilihan() 
        print('') 
    else: 
        print ('Terima Kasih !') 
        exit 

def pilihan(): 
    x = input ("Masukan Pilihan : ") 
    if x == 1: 
        mk = makanan() 
    pil=1 
    while pil !=4: 
        print ("Pilih Makanan 1. Paket Bento A 2. Paket bento B 3. Paket bento C ") 
        pil = int (input('Masukkan pilihan anda : ')) 
        print 
        if pil == 1: 
            print ("") 
            x = input ('Jumlah porsi : ') 
            mk.bentoA(x) 
            pil=4 
        
        if pil == 2: 
            print ("") 
            x = input ('Jumlah porsi : ') 
            mk.bentoB(x) 
            pil=4 
        
        if pil == 3: 
            print ("") 
            x = input ('Jumlah porsi : ') 
            mk.bentoC(x) 
            pil=4 
 
        else:
            exit
            print("terima kasih") 
                
menuutama() 
pilihan()

