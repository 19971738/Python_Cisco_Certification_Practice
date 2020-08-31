myList2 = [1,456, 2, 4, 4, 1, 4, 2, 6, 2, 9, 10,10000,42,118,23,14,87,10,64,76,128,6,2,2,2,2,345,12,10,19,56,19,23,13,456,23,14,89,43,89,43,87,10,23,65,8714,6,6,1,1,1,4,5,6,2,2,2,10,23,9,87,23,65,5,5,5,5,5,1,1,1,1,118,1,1,1,1,1,1]
## numero aumentado 10,23,14,87,10,23,14,89,43,89,43,87,10,23,65,87.14,6,6,1,1,1,4,5,6,2,2,2]
a = True
b = (len(myList2)-1)
c = 0
d = 0

while a:
    a = False
    for i in range(b):
        if myList2[i] > myList2[i+1]:
            myList2[i+1] , myList2[i] = myList2[i] , myList2[i+1]
            a = True

a = True
print("Order numbers list is: ",myList2)
b = (len(myList2)-1)
c = 0
d = b
i = 0
##This code above is to eliminate the repeted numbers
while a:
    a = False
    for e in range(b):
        i=0
        b = (len(myList2)-1)
        while b > 0 :
            b = d - c
            if myList2[i] == myList2[i + 1]:
                del myList2[i+1]
                a = True
                c = c + 1
                b = d - c
            else:
                a = True
                i+=1
                c = c +1
                b = d - c
print("The list with unique elements only:")
print(myList2)
