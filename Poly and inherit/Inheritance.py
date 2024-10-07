# Inheritance
class user:
    def __init__(self) -> None:
        self.name="akhilesh"
        
class student(user):
    # def __init__(self) -> None:
    #     self.rollno = 100
    def enroll(self):
        print("Enroll in this group")
        
u=user()
s=student()

print(s.name)


