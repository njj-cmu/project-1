from typing import Callable
from Person import Person

class Artist(Person):

    def __init__(self, fname: str, lname: str, age: int, gender: str, bio: str, artist_name: str):
        super().__init__(fname, lname, age, gender, bio)
        self.__artistname = artist_name

        # ID is unique and others must not share the same ID.
        self.__id = None

    def setId(self, id: int):
        assert id is int, "Incorrect id type."
        self.__id = id

    def getId(self) -> int:
        return self.__id 
    
    def getArtistName(self) -> str:
        return self.__artistname 
    
    def __str__(self) -> str:
        return self.__artistname
    
    # Static methods
    @staticmethod
    def compareArtistName(a1: 'Artist', a2: 'Artist') -> int:
        """
            Compares the name of two artists. The artist with a smaller lexicographical value
            will go first. For example, ABBA will go first before AKON since ABBA has smaller lexicographical value than AKON.
        
            :param a1: First artist to compare.
            :param a2: Second artist to compare into.
            :return: -1 if a1 should go first. 0 if both are equal. 1 if a2 will go first.
        """
        return Artist.__compareArtist(a1, a2, Artist.getArtistName)
        
    @staticmethod
    def compareArtistId(a1: 'Artist', a2: 'Artist') -> int:
        """
            Compares the id of two artists. The artist with a smaller id value will go first. Note that 
            no two artists will share the same ID, as explained in the Artist class documentation.
        """
        assert a1.getId() != None, "Invalid artist object given."
        assert a2.getId() != None, "Invalid artist object given."
        return Artist.__compareArtist(a1, a2, Artist.getId)

    @staticmethod
    def __compareArtist(a1: 'Artist', a2: 'Artist', getmethod: Callable) -> int:
        assert isinstance(getmethod, Callable), "Invalid getmethod data type. It must be a callable method from the Artist class."
        # print(attrib)
        if getmethod(a1) < getmethod(a2):
            return -1 
        elif getmethod(a1) > getmethod(a2):
            return 1
        else:
            return 0

a1 = Artist("NJ", "Jomaya", 24, "Male", "Good musician.", "njjx") 
a2 = Artist("CH", "Bautista", 31, "Male", "Good musician.", "chvbx") 
print(Artist.compareArtistName(a1, a2))