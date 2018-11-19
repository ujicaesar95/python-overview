# print ("Selamat datang",'\n')
# print ('1. Lihat menu' + "\n" + '2. Lihat cart' + '\n' + '3. Checkout' + '\n' + '4. Keluar' + '\n')
# n = input("pilih angka : ")
kamusku = input("input  value :  ")
def menu1(kamusku) :
    print("Full Dictionary : ")
   
    print("Key:  Value: ")
 
    for key in kamusku :
        if(str(type(kamusku[key])) == "<class 'str'>") :
            print("  " + key + " '" + kamusku[key] + "'")
        elif(str(type(kamusku[key])) == "<class 'int'>") :
            print("  " + key + "  " + str(kamusku[key]) + "  ")
        print(" ")

menu1(kamusku)
