import json

l=[1,2,3,4]

with open("demo.json","w") as f:
    json.dump(l,f)
    
# example

d={
    "name":"nitish",
    "age":"33",
    "gender":"male"
    
}
with open("demoo.json","w") as f:
    json.dump(d,f)
    
# to open json file
with open ("demoo.json","r") as f:
    d=json.load(f)
    print(d)
    

# Serialization and deserialization of the objects made by ourselfs
# we can serialize the python data types that are already given to us but cannot serialize the own made classes
# example
class Person:
     def __init__(self,fname,lname,age,gender) -> None:
         self.fname=fname
         self.lname=lname
         self.age=age
         self.gender=gender
         
        #  format by which it has to be printed is
        # Nitish Singh age -> 33 gender -> male
# object
person=Person("Nitish","singh",33,"male")

# to do the serialization of the object that we just created we make an meathod
def showobject(person):
    if isinstance(person,Person):
        return "{} {} age-> {} gender -> {}".format(person.fname,person.lname,person.age,person.gender)
with open("demo.json","w") as f:
    json.dump(person,f,default=showobject)
    
# deserialization
with open("demo.json","r") as f:
    d=json.load(f)
    print(d)