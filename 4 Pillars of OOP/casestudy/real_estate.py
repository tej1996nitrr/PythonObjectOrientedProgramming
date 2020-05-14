#%%
class Property:
    def __init__(self, square_feet="", beds ="",baths="",**kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths
    def display(self):
        print("Property Details")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))

    @staticmethod
    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),beds=input("Enter number of bedrooms: "),baths=input("Enter number of baths: "))

def get_valid_input(self,input_string, valid_options):
        input_string += " ({}) ".format(", ".join(valid_options))
        response = input(input_string)
        while response.lower() not in valid_options:
            response = input(input_string)
        return response

class Apartment(Property):
    valid_laundries = ("machine","maid","none")
    valid_balconies = ("yes","no","none")
    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    

    @staticmethod 
    def prompt_init():
        parent_init = Property.prompt_init() 
        laundry = get_valid_input("What laundry facilities does the property have? ",Apartment.valid_laundries)
        balcony = get_valid_input("What balcony facilities does the property have? ",Apartment.valid_laundries)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
            })
        return parent_init
class House(Property):
    valid_garage=("attached","detached","none")
    valid_fence = ("yes","no")
    
