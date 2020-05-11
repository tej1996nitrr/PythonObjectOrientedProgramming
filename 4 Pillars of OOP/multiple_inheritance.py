#%%
"""
The simplest and most useful form of multiple inheritance is called a mixin
A mixin is generally a superclass that is not meant to exist on its own, but is meant to be
inherited by some other class to provide extra functionality"""

# %%
from inheriting_contacts import Contact
class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact,AddressHolder):
    def __init__(self, name, email,phone, street, city,state,code):
        Contact.__init__(self,name, email)
        AddressHolder.__init__(self,street,city,state,code)
        self.phone = phone


# %%
class BaseClass:
    num_base_calls=0
    def call_me(self):
        print("Calling base class method")
        self.num_base_calls+=1

class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Left Subclass")
        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Right Subclass")
        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling method on Subclass")
        self.num_sub_calls += 1
s = Subclass()
s.call_me()
#base class's call_me method being called twice.
print(s.num_base_calls,s.num_left_calls,s.num_right_calls,s.num_sub_calls)


# %%
class BaseClass:
    num_base_calls=0
    def call_me(self):
        print("Calling base class method")
        self.num_base_calls+=1

class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls += 1
s = Subclass()
s.call_me()
print(s.num_base_calls,s.num_left_calls,s.num_right_calls,s.num_sub_calls)

"""the super call is not calling the method on the
superclass of LeftSubclass (which is BaseClass). Rather, it is calling RightSubclass,
even though it is not a direct parent of LeftSubclass! This is the next method, not
the parent method. RightSubclass then calls BaseClass and the super calls have
ensured each method in the class hierarchy is executed once."""

# %%
