from List.ArrayList import ArrayList
from Artist import Artist

class Artists(ArrayList):
    """
        Create a storage for artists.
    """

    def __init__(self):
        super().__init__(Artist)
        self.__idgen = 1
    
    def addArtist(self, artist: Artist):
        """
            Adds a new artist into this array list.
        """
        try:
            if self._insert(artist):
                print("Artist successfully added!")
        except AssertionError as ex:
            print(ex)

    def removeArtist(self, attrib : str, val: str | int):
        """
            Removes an artist based on their attribute. Could be their ID or based on their 
            artist name.

            :param attrib: Attribute used for referencing the attribute to use when removing a specific artist.
            :param val: Value of that attribute. Can be a string or an integer (for their ID).
        """

    def sortByArtistName(self, new_copy = False):
        """
            Sorts this list based on the artist's artist name. Assume that no two artists share the same name.

            :param new_copy: Set to True if a new deepcopied artist list should be returned.
            :return: A deep copy of this list of artists if a new copy is required. None otherwise.
        """
        return self._sort()
    

artists = Artists()
