# Define the file path where the text file is located
# Using 'r' before the string ensures it's treated as a raw string (backslashes are not escape characters)
file_path = r"C:\Users\singh\OneDrive\Desktop\Python\7-File Input and Output\2demo.txt"

# Using the 'with' block to open the file in read mode ('r')
# The 'with' block ensures the file is automatically closed after the block is exited
with open(file_path, "r") as f:
    # Read the entire content of the file into the variable 'data'
    data = f.read()
    
    # Print the file content to the console for verification
    print(data)
    # print(type(data))

# Note: There is no need to explicitly call f.close(), as the 'with' block takes care of closing the file automatically


