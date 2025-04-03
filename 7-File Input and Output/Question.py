# Question 1.
# Create a new file "practice.txt" using python. Add the folling data in it.
    # Hi everyone
    # we are learning File I/O
    # using Java.
    # i like programming in Java.


with open("7-File Input and Output\\practice.txt", "w") as f :
    f.write("Hi everyone")
    f.write("\nwe are learning File I/O")
    f.write("\nusing Java.")
    f.write("\ni like programming in Java")




# Question 2.
# WAF that replace all occurences of "java" with "python" in above file.


with open("7-File Input and Output\\practice.txt", "r") as f :
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("7-File Input and Output\\practice.txt", "w") as f :
    f.write(new_data)



# Question 3.
# Search if the word "learning" exist in the file or not.


word = input("Enter the word : ")
with open("7-File Input and Output\\practice.txt", "r") as f :
    data = f.read()
    if(data.find(word) != -1) :
        print("Found")
    else:
        print("Not found")

        # OR
def check_word():
    word = input("Enter the word : ")
    with open("7-File Input and Output\\practice.txt", "r") as f :
        data = f.read()
        if(data.find(word) != -1) :
            print("Found")
        else:
            print("Not found")
check_word()




# Question 4. 
# WAF to find in which line of the file does the word "learning" occur first. Print -1 if word not found.

def check_line():
    word = input("Enter the word : ")
    data = True
    line_no = 1
    with open("7-File Input and Output\\practice.txt", "r") as f :
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
print(check_line())



# Question 5.
# From a file contaning numbers separated by comma, print the count of even numbers .

count = 0
with open("7-File Input and Output\\practice.txt", "r") as f :
    data = f.read()
    # print(data)   # 1, 2, 76, 84, 90, 101

    nums = data.split(",")
    # print(nums)  # ['1', ' 2', ' 76', ' 84', ' 90', ' 101']
    for val in nums :
        if(int(val) % 2 == 0) :
            count +=1
print(count)