# Lists
# A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0–9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don’t have to be related in any particular way. Because a list usually contains more than one element, it’s a good idea to make the name of your list plural, such as letters, digits, or names.
# In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas .

mark1 = 94.5
mark2 = 87.5
mark3 = 90.5
mark4 = 89.5
mark5 = 88.5

mark = [mark1, mark2, mark3, mark4, mark5]
print(mark)
print(type(mark)) # <class 'list'>
print(mark[0]) # 94.5
print(mark[1]) # 87.5  
print(len(mark)) # 5
print(sum(mark)) # 450.5