# Encapsulation

# Topic 1: the instance variables
class Person:
    def __init__(self,name,country) -> None:
        self.name=name
        self.country=country
        
p1=Person("akhilesh","india")
p2=Person("akhilesh","Australia")

print(p1.name , p1.country)
print(p2.name , p2.country)


# 