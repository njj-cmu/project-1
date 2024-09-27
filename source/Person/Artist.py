import datetime
from Person import Person

class Artist(Person):

    def __init__(self, fname: str, lname: str, age: str, gender: str, bio: str, artist_name: str, debuted: str):
        assert datetime.datetime.strptime(debuted, "%d/%m/%y")
        pass



artist = Artist("a","b","c","Male","AAAAA","Dippy","12/12/1000")