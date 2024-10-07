# Aggreation Examples
class Customer:
    def __init__(self,name,gender,address) -> None:
        self.name=name 
        self.gender=gender
        self.address=address
        
    def print_address(self):
        print(self.address.city,self.address.pincode,self.address.state)
        
    def edit_profile(self,new_name,new_city,new_state,new_pincode):
        self.name=new_name
        # what we are doing here is that making sure all the code is picked from the address class
        self.address.edit_address(new_city,new_state,new_pincode)
# since the name and gender are preety straight forward
# but address has various factors like pincode , city , state , housenumber etc

class address:
    def __init__(self,city,state,pincode) -> None:
        self.city=city
        self.state=state 
        self.pincode=pincode
        
    # let say we need to make something to modify our code nd values in it
    # we create a meathod called as edit_class
    def edit_address(self,new_city,new_state,new_pincode):
        self.city=new_city
        self.state=new_state
        self.pincode=new_pincode
        
    # we take all these values and make that go in the customer class
    
        
        
add1=address("jalandhar","punjab",1440078)
cust=Customer("akhilesh","male",add1)

cust.print_address()

# for new class
cust.edit_profile("akhileshhhhhhhh","Rajasthan","123456789","tajaisktan")
# printing after modificaton
cust.print_address()


############### INHERITANCE ##############################

