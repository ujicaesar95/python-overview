# listData = ["Merdeka", "Hello", "Hellos", "Sohib", "Kari ayam"]
# print(listData)
# inputUser = input("Search : ")

# def searchList(keyWord, theList) :
#     newList = list(filter(lambda item: keyWord.lower() in item.lower(), theList))
#     return newList

# searchedList = searchList(inputUser, listData)
# print(searchedList)

# Map & Filter

def mapini(func, theList) :
    newList = []
    for item in theList :
        newList.append(func(item))
    
    return newList

def filterini(func, theList) :
    newList = []
    for item in theList :
        if(func(item)):
            newList.append(item)

    return newList

listTest = [1,2,3,4,5]

list1 = mapini(lambda item: item*2, listTest) #map buat sendiri
list2 = filterini(lambda item: item % 2 == 0, listTest) #filter buat sendiri
list3 = list(map(lambda oy : oy*2, listTest)) #map bawaan python
list4 = list(filter(lambda oy : oy % 2 == 0, listTest)) #filter bawaan python

print("list1 =" + str(list1))
print("list2 =" + str(list2))
print("list3 =" + str(list3))
print("list4 =" + str(list4))


