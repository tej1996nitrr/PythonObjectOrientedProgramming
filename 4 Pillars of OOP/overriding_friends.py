#%%
from  inheriting_contacts import Contact
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name,email)
        self.phone = phone

f = Friend("Harry Potter","hp@gmail.com",123123)
print(f.all_contacts)
print(f.name,f.email,f.phone)


# %%
