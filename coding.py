 #qn 1
list1 = [100, 200, 300, 400, 500]
list1.reverse() #reverse of a list in python
print(list1)
#qn 2
list1 = ["M", "na", "i", "Ke"] #adding two lists index wise
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)] #use the zip() function
print(list3)
#qn 3
numbers = [1, 2, 3, 4, 5, 6, 7]
squared_numbers = [number**2 for number in numbers]
print(squared_numbers)
#qn 4
list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
res = [x + y for x in list1 for y in list2 ]
print(res)
#qn 5
list1 = ["Mike", "Emma", "Kelly", "" , "Brad"]
list1 = list(filter(None, list1))  #using filter() function
print(list1)
#qn 6
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#understanding index,
#list1[0] = 10
#list1[1] = 20
#list1[2] = [300, 400,[5000, 6000], 500]
#list1[2][2] = [5000, 6000]
list1[2][2].append(7000)
print(list1)
#qn 7
list1 = ["a","b", ["c", ["d", "e", ["f", "g"],"k"],"l"],"m", "n"]
#understanding indexing
#list1[2] = ["c", ["d", "e",["f","g"],"k"], "l"]
#list1[2][1] = ["d", "e",["f","g"], "k"]
#list1[2][1][2] = ["f","g"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)
#qn 8
list1 = [5, 10, 15, 20, 25, 50, 20]
#get the first occurence index
index = list1. index(20)
list1[index] = 200  #updating item present at location
print(list1)
#qn 9
list1 = [5, 20, 15, 20, 25, 50, 20]
list1 = list(filter((20).__ne__, list1))
print(list1)
#qn 10
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
# the zip()function
for x, y in zip (list1, list2[::-1]):   #reverse list using list slicing
    print(x, y)