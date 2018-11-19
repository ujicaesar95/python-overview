#FizzBuzz

# num = int(input("input number : "))

# def fizzbuzz(num) :
#     for i in range(1, num+1) :
#         if(i % 3 == 0 and i % 5 == 0):
#             print("FizzBuzz")

#         elif (i % 3 == 0):
#             print("Fizz")
        
#         elif(i % 5 == 0):
#             print("Buzz")
    
#         else :
#             print (i)

# fizzbuzz(num)

#fibonacci

# x = int(input("x = "))
# listdata = [""]
# def fibo(z):
#     for i in range(1)

x = int(input("x = "))
def fibo(urut):
    data = []
    for i in range (urut):
        if(i == 0):
            data.append(0)
        elif(i < 2):
            data.append(1)
        else :
            data.append(data[i-2] + data[i-1])
    return data

print(fibo(x))

###
beru = [1,2,3,4,5]
biru = beru.copy()

biru.append(6)

print("beru = " + str(beru))
print("biru = " + str(biru))

####

beoru = ["a","b","c","d","e"]
for i, item in zip(range(3), beoru):
    print(i, item)



        

