# # no 1

inputnum = int(input("masukan nilai : "));
# if (inputnum % 2 == 0) :
#     print("genap")
# else:
#     print("ganjil")

arr = ["genap", "ganjil"]
print("angka {} tergolong bilangan {}".format(inputnum, arr[inputnum%2]))
# no 2

massa = int(input("massa(kg) = "))
tinggi = int(input("tinggi(cm) = "))
imt = ((massa/(tinggi/100)**2))

if (imt < 18.5) :
    print("imt anda {} berarti berat badan kurang".format(imt))
elif (18.6 <= imt and imt <= 24.9) :
    print("imt anda {} berarti berat badan ideal".format(imt))
elif(25 <= imt and imt <= 29.9) :
    print("imt anda {} berarti BB berlebih".format(imt))
elif(30.0 <= imt and imt < 39.9) :
    print("imt anda {} berarti BB sangat berlebih".format(imt))
else :
    print("imt anda {} berarti obesitas".format(imt))


