# nomer 1
x = 4;
y = 3;
z = 2;

w = float(((x + (y*z))/(x * y))**z) ;

x1 = str(x);
y1 = str(y);
z1 = str(z);
w1 = str(w);
print("x = " + x1);
print("y = " + y1);
print("z = " + z1);
print("w = ((x + (y*z))/(x * y))**z = " + w1);

#nomer 2
import math;
number = input("input number : ");
number1 = (math.pow(int(number), 2));
strnumber = str(number);
strnumber1 = str(number1);


print("kuadrat dari " + strnumber + " = " + strnumber1);

#nomer 3

tahun1 = 360 ; 
bulan1 = 30 ;
minggu1 = 7 ;

inputnum = 485 ;

hasil1 = inputnum - tahun1;
hasil1a = inputnum / tahun1;
hasil1b = (math.floor(hasil1a))
tahun = str(hasil1b);

hasil2 = hasil1 / bulan1;
hasil2a = (math.floor(hasil2));
bulan = str(hasil2a);

hasil3 = hasil2 / minggu1;
hasil3a = (math.floor(hasil3));
minggu = str(hasil3a);

hasil4 = (hasil1 - (bulan1 * hasil2a));
hari = str(hasil4); 

print(tahun + " tahun " + bulan + " bulan " + minggu + " minggu " + hari + " hari ");

#nomer 4

# rasio umur andi & budi = 0.4
# jumlah umur mereka 49 th
# Andi = 4 & Budi = 10

a = 4;
b = 10;
jumlahUmur = 49;
jumlah = a + b ;
umurA = ((a/jumlah)*jumlahUmur);
umurB = ((b/jumlah)*jumlahUmur);

umurAnow = umurA + 2;
andi = str(umurAnow);
umurBnow = umurB + 2;
budi = str(umurBnow);

print("Umur Andi = " + andi + " tahun & umur Budi = " + budi + " tahun ");

#nomer 5

wordnya = "Halo Dunia";
count = wordnya.split("a");

print( wordnya + " = " + str(len(count)-1))


#nomer 6
# jarak a & b 120km = 120.000 m
# a = 60 km/h & b = 40 km/h 
# start 9:00:00

start = 9 * 60
s = 120000
va1 = 60*1000/3600;
va = str(va1);
ta1 = s / va1;
ta = str(ta1);

vb1 = 40*1000/3600;
vb = str(vb1);
tb1 = s / vb1;
tb = str(tb1);

tnabrak1 = tb1 - ta1;
tnabrak = str(tnabrak1);

ttabrak = tnabrak1 / 60;
menittabrak = start + ttabrak;
jamtabrak1 = menittabrak / 60;
jamtabrak = str(jamtabrak1);


print("va = " + va + " m/s vb = " + vb + " m/s ");
print("ta = " + ta + " s tb = " + tb + " s ");
print("tnabrak = " + tnabrak + " s ");
print("waktu bertabrakan = jam " + jamtabrak);