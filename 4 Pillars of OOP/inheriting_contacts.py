#%%

class ContactList(list):
    def search(self,name):
        """Method to search name from contacts"""
        matching_contact=[]
        for contact in self:
            if name in contact.name:
                matching_contact.append(contact)
        return matching_contact
class Contact:
    all_contacts = ContactList() #class variables.
    def __init__(self, name, email):
        self.email = email
        self.name = name
        Contact.all_contacts.append(self) #add functionality to an existing class
    

class Supplier(Contact):
    def order(self,order):
        print(f'Order will be sent to {self.name} and order is {order}')

c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")
print([c.name for c in Contact.all_contacts.search('John')])
# %%class LongNameDict(dict):
class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest
longkeys = LongNameDict()
longkeys['hello'] = 1
longkeys['longest yet'] = 5
longkeys['hello2'] = 'world'
longkeys.longest_key()


# %%
