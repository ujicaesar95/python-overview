# oy = {"aasa" : { "asd " : 10}, "yhu" : 90}

# print(oy.keys())
# print(list(oy.keys()))
# for key in oy.keys() :
#     print(oy[key])

# ###

# def a(num) :
#     return "ini " + str(num*3)

# listnum = [1,2,3,4,5]
# # newList = [a(b) for b in listnum]

# newList = list(map(a,listnum))

# print(newList)

#buat duplikat function dari map dan filter


# def check(num):
#     return num % 2 == 0

# listnum = [1,2,3,4,5]
# newlist = list(map(check,listnum))
# print("list map = " + str(newlist))

# def check(num):
#     return num % 2 == 0

# listnum = [1,2,3,4,5]
# newlist = list(filter(check,listnum))
# print("list filter = " + str(newlist))

# numlist = [1,2,3]
# input = "x"

# check1 = input in numlist
# check2 = "x" in ["x", "y", "z"]
# check3 = "ka" in "kurakas"

# print("value check1 = " + str(check1))
# print("value check2 = " + str(check2))
# print("value check3 = " + str(check3))


list1 = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari ayam']
search = input('search kata = ')

def searchlist(keyword, list1):
    newlist = list(filter(lambda item : keyword.lower() in item.lower(), list1))
    return newlist

hasilsearch = searchlist(search, list1)

print(list1)
print(hasilsearch)

dicky = { }
dicky["Paket Bento B"] = 1
print(dicky)


#tugas
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






# coba1 = "ka" in strlist1
# coba2 = "hel" in strlist1
# strcoba1 = str(coba1)
# strcoba2 = str(coba2)
# newlist1 = list(filter(strcoba1,strlist1))
# newlist2 = list(filter(strcoba2,strlist1))



# print(strlist1)
# print("value newlist1 = " + str(newlist1))
# print("value newlist2 = " + str(newlist2))
# print("value coba1 = " + str(coba1))
# print("value coba2 = " + str(coba2))

