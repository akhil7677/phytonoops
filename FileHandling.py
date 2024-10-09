# File handling 

# Writting to a file:

    # case 1- if the file is not present(we make a file and then write in that file)
    
# what we just did here is made a file 
# we used the f open option for it gave it a file name and further opened it in write mode
# also we can write in that file using "f.write"
f=open("sample.txt",'w')
f.write("Hellow world")
f.close()# to close our opened file
# since file is closed hence no new wirte operation will work on this
# f.write("hi")
# this code wont work


################### Case 2: Write Multiline Strings ######################
f=open("Sampletext.txt","w")
f.write("hello how are you ?")
f.write("\nhi i am fine tell me about yourself")
f.close()

# case 3 : wite a file on existting file

# in this case a new file that has been created replaces the orginal contents of the file that was created above
f=open("sample.txt","w")
f.write("Salman Khan")
f.close()



# Problem with the " w " mode

# let say i want to add third line in the "Sampletext.txt" file
# instead of using the "w" mode just use the "a" mode

f=open("/home/akhilesh/Desktop/Python OOPs/Sampletext.txt" , "a")
f.write("\nhello boys i like my girlfirend 'Sammmyyyyyyy' ")
f.close()

# Passing an entire list in a file USE WRITE LINES
l=["hi\n","hap\n","no no\n"]
f=open("/home/akhilesh/Desktop/Python OOPs/Sampletext.txt","a")
f.writelines(l)


        # reading form a file
f=open("/home/akhilesh/Desktop/Python OOPs/Sampletext.txt","r")
s=f.read()# you can actually define how many characters you want it to read it from here
print(s)
f.close()


# readding a code line by line
# we use the "readline function to define how we will read the text line by line"
f=open("/home/akhilesh/Desktop/Python OOPs/Sampletext.txt","r")
t=f.readline()
p=f.readline()
f.close()
print(t,p)
# when we will use read and when will we use readlines?
# Ans)we use readlline when file is having alot of content and we dont want to push all of the the file in the memory thus we dont want to overload the memomry



# How to read entire files in python
# below is the code how
# Always use this code below to read files
f=open("/home/akhilesh/Desktop/Python OOPs/Sampletext.txt","r")
while True:
    data=f.readline()
    if data == '':
        break
    else:
        print(data)
f.close()
# Always use this code below has ended


                                            # With Keyword #
# it is a good idea to close our file after we are done editing it
# if we donot close it garbage collector will close it automatically
# with the "with" keyword the file gets closed automatically

with open("/home/akhilesh/Desktop/Python OOPs/Sampletext.txt","a") as f:
    f.write("New Selmon Bhai")
    
# with open("/home/akhilesh/Desktop/Python OOPs/Sampletext.txt","r") as f:
#     # print(f.read()


# taking data from a big files in chunks
# step1: created a file that has alot of big data
big_L=["hello world" for i in range (1000)]

# with open("bigtext.txt","w") as f:
#     f.write("hollo")
    
# # opening the file in chunks
# with open("bigtext.txt","r") as f:
#     # chunk size
#     # defining a size here that will the size of the chunks that will be loaded when ever the data is enetered
#     chunk_size=10
#     while len(f.read(chunk_size)>0):#used the while loop to load the values by 10
#         print(f.read(chunk_size),end="***")#printing the values
#         f.read(chunk_size)#break statement for the loop        


# seek and tell functions
# tell functions tell us where the cursor is at the next position
# seek function helps us to take the cursor to where ever we want in our file
with open("Sampletext.txt","w") as f:
    f.write("hello")
    f.seek(0)
    f.write("xa")
    
# Working with images (you cannot work with images simply because texxt data is unicode data and images is binary data)
# to work with that we gotta do is

# working with bianary files
# you gotta use the rb option "rb is read bianary"
# you gota make a copy and then use it
with open("qp.png","rb") as f:
    with open("qp_copy.png","wb") as wf:
        wf.write(f.read())
        
# problems of workinng with text files is that we cannot store other data types like int flot etc
with open("sample.txt","r") as f:
    # this will throw and error because the with only works with the string type
    # you can use the type conversion meathod to solve this but type has to be converted to string only always
    f.write("5")
    
# in conclusion we can never store a complex text file with diffrent data types as a file

