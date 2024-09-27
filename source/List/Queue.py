from Playlist import Track
from ArrayList import ArrayList

class Queue(ArrayList):

    def __init__(self, data: type):
        super().__init__(data, 50)

    def addToQueue(self, track: Track) -> bool:
        super().insert()