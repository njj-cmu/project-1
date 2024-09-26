from List.ArrayList import ArrayList


#
# def asc(a: int, b: int) -> int:
#     if a < b:
#         return -1
#     elif a > b:
#         return 1
#     else:
#         return 0
#
#
# def desc(a: int, b: int) -> int:
#     if a < b:
#         return 1
#     elif a > b:
#         return -1
#     else:
#         return 0
#
#
# arr = ArrayList(int)
#
# arr.insert(1)
# arr.insert(10)
# arr.insert(20)
# arr.insert(15, 2)
# arr.insert(17, 2)
# arr.insert(100)
# arr.insert(-1)
#
# arr.removeOnValue(15)
# arr.removeOnValue(15)
#
# arr.sort(desc, False)
# copy = arr.sort(asc, True)
#
# print("Arr copy: ", copy)
# print("Original: ", arr)
# copy.update(1000, 1)

class Person:

    def __init__(self, fname: str, lname: str, height: float, weight: float, income: float, age: int):
        self.__fname = fname
        self.__lname = lname
        self.__height = height
        self.__weight = weight
        self.__income = income
        self.__age = age

    def getFName(self) -> str:
        return self.__fname

    def getLName(self) -> str:
        return self.__lname

    def getHeight(self) -> float:
        return self.__height

    def getWeight(self) -> float:
        return self.__weight

    def getTax(self) -> float:
        return self.__income * 0.05

    def getAge(self) -> int:
        return self.__age

    def getBMI(self) -> float:
        return round(self.getWeight() / (self.getHeight() ** 2), 2)

    def getIncome(self) -> float:
        return self.__income

    @staticmethod
    def compareAge(p1: 'Person', p2: 'Person') -> int:
        if p1.getAge() < p2.getAge():
            return -1
        elif p1.getAge() == p2.getAge():
            return 0
        else:
            return 1

    @staticmethod
    def compareLName(p1: 'Person', p2: 'Person') -> int:
        if p1.getLName() < p2.getLName():
            return -1
        elif p1.getLName() == p2.getLName():
            return 0
        else:
            return 1

    @staticmethod
    def compareBMI(p1: 'Person', p2: 'Person') -> int:
        if p1.getBMI() < p2.getBMI():
            return -1
        elif p1.getBMI() == p2.getBMI():
            return 0
        else:
            return 1

    def __str__(self):
        return f"{self.getLName()} - {self.getFName()}"
        # return (f"{self.getFName()} {self.getLName()}, aged {self.getAge()} years old, with a BMI of "
        #         f"{self.getBMI()}, having an income of {self.getIncome()}, taxed yearly by {self.getTax()}")


arr = ArrayList(Person)

arr.insert(Person("Neil John", "Jomaya", 1.69, 110, 29165.00, 24))
arr.insert(Person("Charles Hanz", "Bautista", 1.69, 85, 29165.00, 31))
arr.insert(Person("Eyeryl Jun", "Tano", 1.60, 78, 32333.00, 28))

print("Original placement: ", arr)
arr.sort(Person.compareLName)

print(arr)