# Rule no. 1:
'''
a,b = 2,3
txt = "@"
print(2*txt*3)
'''
#output: @@@@@@


# Rule no. 2:
'''
a,b = "2",3
txt = "@"
print((a+txt)*b)
'''
#output: 2@2@2@


# Rule no. 6:
'''
a,b = 1.5,3
c = a//b 
print(c , a/b)
'''
# // is used for floor division ( floor gives closest integer less or egual to float value )
# / is used for normal division
# output: 0 0.5

a,b = -5,2
c = a%b
print(c)
# output: 1

a,b = 5,2
c = a%b
print(c)
# output: 1

a,b = 5,-2
c = a%b
print(c)
# output: -1
