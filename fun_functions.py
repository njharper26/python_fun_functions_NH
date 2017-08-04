def funWFunctions(start, end):
    for count in range(start, (end + 1)):
        if count % 2 == 0:
            print count, "This is an even number."
        else:
            print count, "This is an odd number."
            
funWFunctions(1, 2000)


def multiply(lst, fact):
    for i in range(0, len(lst)):
         lst[i] *= fact
    
    return lst

lst = [2, 4, 10, 16]
fact = 5

print multiply(lst, fact)


def layeredMultiples(lst1):
    print lst1
    lst2 = []
    for x in lst1:
        val_lst1 = []
        for i in range(0, x):
            val_lst1.append(1)
        lst2.append(val_lst1)
    
    return lst2

print layeredMultiples(multiply(lst, fact))

