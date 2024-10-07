class Person:
    def __init__(self,name,gender) -> None:
        self.name=name
        self.gender=gender
        
# outside class function
def greet(person):
    person.name="ankit"
    return person

p=Person("nitish","male")
print(id(p))
print(id(greet(p)))