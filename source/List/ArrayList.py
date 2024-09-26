from typing import Callable
import copy


class ArrayList:
    """
    An array list data structure that stores data based on a particular type.
    """

    def __init__(self, data: type, size: int = 50):
        """
        Creates a new array list of specific size, while only accepting values from an object type.
        :param data: Type of data this array list will store only.
        :param size: Defaults to 50.
        """
        assert isinstance(data, type), "Data type must be of correct type."
        # assert data.__str__ is not object.__str__, "Data type must have implemented the __str__ method."
        self.__arr = [None] * (size - 1)
        self.__data = data
        self.__size = 0

    def getSize(self) -> int:
        return self.__size

    def __increaseSize(self):
        self.__size += 1

    def __decreaseSize(self):
        self.__size -= 1

    def __increaseListSize(self):
        """
        Increases the size of this list by 2 when full.
        :return:
        """
        self.__arr += [None] * ((self.getSize() * 2) - 1)

    def getDataType(self):
        return self.__data

    def _checkDataType(self, item: any) -> bool:
        """
        Checks if the item is an instance of the object of the data type related to this array list.
        :param item:
        :return: True if it is an instance. False if not.
        """
        return isinstance(item, self.getDataType())

    def get(self, pos: int) -> any:
        return self.__arr[pos]

    def insert(self, item: any, pos: int = -1):
        """
        Inserts a new item of the object type to the specified position. Defaults to insert at last.
        :param item: Item to be inserted.
        :param pos: Position to insert into. Must not exceed current number of elements of array list.
        :return: Nothing.
        """
        assert self._checkDataType(item), "Incorrect data type of item given."
        assert pos < self.getSize(), "Invalid position."

        # Check if Array List is full
        if self.__size >= len(self.__arr):
            self.__increaseListSize()

        pos = self.getSize() if pos == -1 else pos

        self.__adjust(self.getSize(), pos, "f")

        self.__arr[pos] = item
        self.__increaseSize()

    @staticmethod
    def setAdjustCondition(counter: int, sentinel: int, operator: str) -> bool:
        match operator:
            case ">":
                return counter > sentinel
            case "<":
                return counter < sentinel
            case ">=":
                return counter >= sentinel
            case "<=":
                return counter <= sentinel
            case "==":
                return counter == sentinel
            case "!=":
                return counter != sentinel
            case _:
                raise ValueError("Incorrect value given.")

    def __adjust(self, start: int, end: int, d: str) -> None:
        """
        Adjusts the array list based on direction.
        :param start: Starting index of adjustment.
        :param end: Last index of adjustment.
        :param d: Direction of adjustment. 'f' to let index ahead have value of previous index. 'b'
            to let index behind have value of next index.
        :return:
        """
        assert d.casefold() == "f" or d.casefold() == "b", "Incorrect direction."
        assert 0 <= start <= self.getSize(), "Start index out of bounds."
        assert 0 <= end <= self.getSize(), "End index out of bounds."

        d = d.lower()

        operator = ">=" if d == "f" else "<="

        while ArrayList.setAdjustCondition(start, end, operator):
            if d == "f":
                self.__arr[start] = self.__arr[start - 1]
                start -= 1
            else:
                self.__arr[start] = self.__arr[start + 1]
                start += 1

    def update(self, value: any, pos: int) -> bool:
        """
        Updates the element at the index with a new element.
        :param value: New value to replace at index.
        :param pos: Index of element to be updated.
        :return: Flag if update was done or not.
        """
        assert 0 <= pos < self.getSize(), "Index of element out of bounds."
        self.__arr[pos] = value

        return True

    # def updateItem(self, value: any, setter: Callable[..., None], pos: int) -> bool:
    #     """
    #     Updates a particular value from an item using a callable set method.
    #     :param setter: Setter method required to modify value of an attribute from the element.
    #     :param value: New value to replace.
    #     :param pos: Position to update into.
    #     :return: Flag if update was successful or not.
    #     """
    #     pass

    def remove(self, pos: int) -> any:
        """
        Removes an item from the position of this list.
        :param pos: Position of item to be removed. Must be within 0 and size of this array - 1.
        :return: The item that was removed.
        """
        assert isinstance(pos, int), "Invalid position type given."
        assert 0 <= pos < self.getSize(), "Removal index out of bounds."

        item = self.get(pos)
        self.__adjust(pos, self.getSize(), "b")
        self.__decreaseSize()
        return item

    def removeOnValue(self, value: Callable | int | float | str) -> any:
        """
        Removes an item based on the given method to retrieve its value.
        :param value: Method to retrieve value from the array list, or can be an absolute value 
            such as integer, float, or string.
        :return: Item if it exists based on value. None if it does not.
        """
        assert isinstance(value, (Callable, int, float, str)), "Invalid data type of value given."

        target = None

        for i in range(self.getSize()):
            try:
                # Check if target is callable
                target = value()
            except:
                # If it is not callable, try setting as primitive value.
                target = value
            finally:
                if self.get(i) == target:
                    return self.remove(i)

        # If loop terminates, that means that the element with such value was not found.
        print("Item to be removed not found.")
        return None

    def sort(self, comparator: Callable[[any, any], int], new_copy: bool = False) -> 'ArrayList':
        """
        Sorts this array list based on some comparison. May create a sorted copy or not. Utilizes selection sort.
        :param comparator: Comparison method used for sorting elements. The comparison method
            must always be in the form: compare(a, b,), and must return an int between the following: -1, 0, and 1.
        :param new_copy: Flag if this sort operation should produce a copy and not compromise the original array.
        :return:
        """
        l = deepcopy(self) if new_copy else self

        for i in range(0, l.getSize()):
            idx = i
            for j in range(i, l.getSize()):
                if comparator(l.get(j), l.get(idx)) < 0:
                    idx = j

            temp = l.get(i)
            l.update(l.get(idx), i)
            l.update(temp, idx)

        return l

    def __str__(self) -> str:
        s = "[ "

        for i in range(self.getSize()):
            s += str(self.get(i))

            if (i + 1) < self.getSize():
                s += ", "

        s += " ]"

        return s


def deepcopy(source: ArrayList) -> ArrayList:
    """
        Creates a deep copy from one array list to the other array list.
    """
    arr = ArrayList(source.getDataType(), source.getSize())

    # Insert each item
    for i in range(source.getSize()):
        arr.insert(source.get(i))

    return arr
