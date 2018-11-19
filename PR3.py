#coba1
#
##
###

# coba1 = int(input("coba1 input number : "))
# for i in range(1,coba1+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# print("Number of rows: ",coba1)

#nomer 1
###
##
#

# MB1 = int(input("solve 1 input number : "))
# for i in range(MB1,0,-1):
#     for j in range(0,i):
#         print("*", end= " ")
#     print()
# print("Number of rows: ",MB1)

#nomer 2
###
##
#
##
###

# MB2 = int(input("solve 2 input number : "))
# for i in range(MB2,0,-1):
#     for j in range(0,i):
#         print("*", end= " ")
#     print()
# for x in range(MB2-1):
#     for y in range(x+2):
#         print("*",end=" ")
#     print()
# print("Number of rows: ",MB2*2-1)
    

#nomer 3
   #
  ###
 ##### 

# MB3 = int(input("solve 3 input number : "))
# for i in range(0,MB3):
#     for j in range(0,MB3-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()
# print("Number of rows: ",MB3)

#versi 3.2

# size = int(input("masukan angka :"))
# z = ""
# for num in range(size):
#     for num1 in range(size-1-num):
#         z += "   "
#     for num2 in range((num*2)+1):
#         z += " * "
#     z += "\n"

# print(z)


#nomer 4
#####
 ###
  #
  
# MB4 = int(input("solve 4 input number :"))
# for i in range(MB4,0,-1):
#     for j in range(0,MB4-i):
#         print(end=(" "))
#     for j in range(0,i):
#         print("*",end=" ")
#     print()
# print("Number of rows: ",MB4)

#versi 4.2
# size = int(input("masukan angka :"))
# z = ""
# for num in range(size):
#     for num1 in range(num):
#         z += "   "
#     for num2 in range((size*2)-(num*2)-1):
#         z += " * "
#     z += "\n"

# print(z)

#nomer 5
    #
   ###
  #####
   ###
    # 

# MB5 = int(input("solve 5 input number :"))
# def diamond(trp):
#   for i in range(trp):
#     print(" "*(trp-i-1) + "* "*(i+1))
#   for j in range(trp-1,0,-1):
#     print(" "*(trp-j)+ "* "*j)
#   print("Number of rows:",trp*2-1)
# diamond(MB5)

#versi 5.2

# size = int(input("masukan angka :"))
# z = ""
# for num in range(size):
#     for num1 in range(size-1-num):
#         z += "   "
#     for num2 in range((num*2)+1):
#         z += " * "
#     z += "\n"
# for num in range(1, size):
#     for num1 in range(num):
#         z += "   "
#     for num2 in range((size*2)-(num*2)-1):
#         z += " * "
#     z += "\n"

# print(z)

# diamon terbalik


size = int(input("masukan angka :"))
z = ""
for num in range(size):
    for num1 in range(size-num):
        z += " * "
    for num2 in range((num*2)+1):
        z += "   "
    z += "\n"
for num in range(1, size):
    for num1 in range(num):
        z += " * "
    for num2 in range((size*2)-(num*2)-1):
        z += "   "
    z += "\n"

print(z)

#pyramid angka

# yuk = int(input("yuk masukin angka : "))
# for i in range(1,yuk+1):
#     for j in range(1,yuk-i+1):
#         print(end=" ")
#     for j in range(i,0,-1):
#         print(j,end="")
#     for j in range(2,i+1):
#         print(j,end="")
#     print()
# print("Number of rows:",yuk)