#%%
from collections import Container
Container.__abstractmethods__
# %%
import abc
class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass
    @abc.abstractproperty
    def ext(self):
        pass
    @classmethod
    def __subclasshook__(cls, subclass):
        """any class that supplies concrete implementations of all the
abstract attributes of this ABC should be considered a subclass of MediaLoader,
even if it doesn't actually inherit from the MediaLoader class."""
        if cls in MediaLoader:
            attrs = set(dir(subclass))
            if set(subclass.__abstractmethods__)<=attrs:
                return True

        return NotImplemented

# class Wav(MediaLoader):
#     pass
# x=Wav()

class Ogg(MediaLoader):
    ext = ".ogg"
    def play(self):
        pass
o = Ogg()

# %%
