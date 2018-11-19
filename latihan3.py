# # listx = ['a',['b', 'c']]

# # for item in listx []:
# #     if(type(item) == type('')):
# #         print(item)
# #     elif(type(item) == type([])):
# #         for menu in item :
# #             print(menu)

# for apapun in range(0,22,2) :
#     print("nomor urut {}".format(apapun))


w = int(input("w = "))
y = int(input("y = "))
def cool_diamond(w):
    r = []
    for y in range(w):
        s = '*' * (w - y)
        r.append("{0}{1}{0}".format(s, ''.join([' ' for x in range(2 * y)]), s))

    return '\n'.join(r + r[::-1])

for i in range(3, 6):
    print (cool_diamond(i))
    print(' ' * 80)

#####
import math
size = int(input("size = "))
def make_diamond(size):
    if not size%2:
        raise ValueError('odd number required')
    r = [' ' * space + '*' + ' ' * (size-2-(space*2)) + '*' + ' ' * space for space in xrange((size-1)/2)]    
    r.append(' ' * ((size-1)/2) + '*' + ' ' * ((size-1)/2))
    return '\n'.join(r[-1:0:-1] + r)
print(make_diamond(size))
