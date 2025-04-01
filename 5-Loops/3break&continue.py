# Break :

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x =int(input("Enter a Number from given Tuple :")) 

i = 0
while i < len(num) :
    if(num[i] == x) :
        print("Found at Index :", i)
        break
    else:
        print("finding....")
    i += 1


# Continue :
i = 0
while i <= 5 :
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1
