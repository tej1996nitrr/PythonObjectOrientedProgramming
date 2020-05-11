#%%
class Contact:
    all_contacts=[] #class variables.
    def __init__(self, name, email):
        self.email = email
        self.name = name
        Contact.all_contacts.append(self) #add functionality to an existing class

class Supplier(Contact):
    def order(self,order):
        print(f'Order will be sent to {self.name} and order is {order}')
c = Contact("Somebody","somebody@gmail.com")
s = Supplier("Supplier","sup@gmail.com")
print(c.name,c.email,s.name,s.email)
print(c.all_contacts)
# print(c.order("I need pliers"))
print(s.order("I need pliers"))

# %%
