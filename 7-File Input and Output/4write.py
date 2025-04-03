# file_path = r"C:\Users\singh\OneDrive\Desktop\Python\7-File Input and Output\2demo.txt" 

# Writing files :
'''
with open(file_path, "w") as f:
    f.write("I am fantastic")
'''

# you can create a file 
# f = open("sample.txt", "w")
f = open("7-File Input and Output\\hello.txt", "w")
f.write("hello")
f.write("\noooo")
f.write("\nlove to spend time with my friends")
f.close()



# Appending files :
'''
with open(file_path, "a") as f:
	f.write("\nI want to become successfull")
'''

# you can create a file 
f = open("7-File Input and Output\\hello.txt", "a")
f.write("hello")
f.write("\noooo")
f.write("\nlove to spend time with my friends")
f.close()