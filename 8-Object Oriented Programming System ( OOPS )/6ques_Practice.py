# Question 1.
# Create student class that takes name & marks of 3 sunjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def get_avg(self):
        sum = 0
        for val in self.mark:
            sum += val
        print("Hii", self.name, "Your avg score is : ", sum/3)

s1 = Student("Tony Stark", [90, 80, 70])
s1.get_avg()


s1.name = "Ironman"
s1.get_avg()