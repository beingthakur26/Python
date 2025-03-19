# single line conditional statement :

food = input (" food : ")
eat = "yes " if food == "cake" else "no "
print(eat)
# Output:
# food : cake
# yes

food = input (" food : ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")
# Output:
# food : cake
# sweet
# Output:
# food : jalebi
# sweet



# Clever if : 

age = int (input("age : "))
# agar age 18 se choti hai to vote no warna yes
vote = ("yes", "no") [age <= 18]
print(vote)