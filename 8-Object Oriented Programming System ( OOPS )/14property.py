class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    # def cal_per(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(90, 80, 70)
print(stu1.percentage)  # Output: 80.0%

stu1.phy = 86
# print(stu1.phy)  # Output: 86
# stu1.cal_per()  # Recalculate percentage after changing phy
print(stu1.percentage)  # Output: 80.0%