# WAP to ask the user to enter names of their 3 favourite movies and store them in a list ? 

movie1 = input("Enter the name of your favourite movie: ")
movie2 = input("Enter the name of your second favourite movie: ")
movie3 = input("Enter the name of your third favourite movie: ")
list = [movie1, movie2, movie3]
print(list) # ['movie1', 'movie2', 'movie3']


# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

list = [1, 2, 3, 2, 1]
list1 = list.copy()
list1.reverse()
if(list == list1):
    print("The list contains a palindrome of elements.")
else:
    print("The list does not contain a palindrome of elements.")


# WAP to count the number of students with the "A" grade in the folling tuple. Store the above values in alist and sort them from "A" to "D".
#["C", "D", "A", "A", "B", "B", "A]

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A")) # 3

list = list(grade)
list.sort()
print(list) # ['A', 'A', 'A', 'B', 'B', 'C', 'D']