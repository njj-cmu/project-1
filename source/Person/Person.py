class Person:

    def __init__(self, fname: str, lname: str, age: int, gender: str, bio: str):
        assert isinstance(fname, str), "Invalid first name data type."
        assert isinstance(lname ,str), "Invalid last name data type."
        assert isinstance(age ,int), "Invalid age data type."
        assert isinstance(bio ,str), "Invalid person biography data type."
        assert gender in ["Male", "Female"], "Invalid gender input. Must be \'Male\' or \'Female\' only."

        self.__fname = fname
        self.__lname = lname 
        self.__age = age 
        self.__gender = gender 
        self.__bio = ""

    def getFName(self) -> str:
        return self.__fname 
    
    def getLName(self) -> str:
        return self.__lname
    
    def getFullName(self) -> str:
        return f"{self.getContraction()} {self.getFName()} {self.getLName()}"
    
    def getAge(self) -> str:
        return self.__age
    
    def getContraction(self) -> str:
        return "Mr." if self.getGender() == "Male" else "Ms."
    
    def getGender(self) -> str:
        return self.__gender
    
    def getBio(self) -> str:
        return self.__bio
    
    def __str__(self) -> str:
        return self.getFullName()