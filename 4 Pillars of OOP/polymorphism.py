#%%
"""Ad-hoc polymorphism through function overloading is not possible in Python. """
class AudioFile:
    def __init__(self, filename):
        """The __init__ method in the parent class is able to access
            the ext class variable from different subclasses.That's polymorphism at work"""
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print("playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print("playing {} as wav".format(self.filename))

class OggFile(AudioFile):
    ext = "ogg"
    def play(self):
        print("playing {} as ogg".format(self.filename))
ogg = OggFile("myfile.ogg")
ogg.play()
mp3 = MP3File("myfile.mp3")
mp3.play()
not_an_mp3 = MP3File("myfile.ogg")
not_an_mp3.play()
# %%
"""Duck typing in Python allows us to use any object that provides the required behavior
without forcing it to be a subclass. The dynamic nature of Python makes this trivial.
The following example does not extend AudioFile, but it can be interacted with in
Python using the exact same interface:"""
class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")
        self.filename = filename
    def play(self):
        print("playing {} as flac".format(self.filename))
#%%
# Duck Typing
class Shark():
    def swim(self):
        print('Shark is Swimming')
    def swim_backwards(self):
        print("shark can't swim backwards")
    def skeleton(self):
        print("sharks skeleton is made of cartilage"
        )
class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")
sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton()

# %%
#Method Overriding -dynamic polymorphism
class Bird: 
    def intro(self): 
        print("There are many types of birds.") 
        
    def flight(self): 
	    print("Most of the birds can fly but some cannot.") 
	
class sparrow(Bird): 
    def flight(self): 
	    print("Sparrows can fly.") 
	
class ostrich(Bird): 
    def flight(self): 
        print("Ostriches cannot fly.") 
	
obj_bird = Bird() 
obj_spr = sparrow() 
obj_ost = ostrich() 

obj_bird.intro() 
obj_bird.flight() 

obj_spr.intro() 
obj_spr.flight() 

obj_ost.intro() 
obj_ost.flight() 


# %%
