# File Reading :

file_path = r"C:\Users\singh\OneDrive\Desktop\Python\7-File Input and Output\2demo.txt" 

with open(file_path, "r") as f:
	
	# data = f.read()
	# print(data)

	line1 = f.readline()
	print(line1)
	
	line2 = f.readline()
	print(line2)
	
	line3 = f.readline()
	print(line3)



# Overwriting file :
f = open("7-File Input and Output\\2demo.txt","r+")
f.write("abc")
print(f.read())
f.close()
