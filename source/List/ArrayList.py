from typing import Callable
from typing import List

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

    def _getSize(self) -> int:
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
        self.__arr += [None] * ((self._getSize() * 2) - 1)

    def _getDataType(self):
        return self.__data

    def _checkDataType(self, item: any) -> bool:
        """
        Checks if the item is an instance of the object of the data type related to this array list.
        :param item:
        :return: True if it is an instance. False if not.
        """
        return isinstance(item, self._getDataType())

    def _get(self, pos: int) -> any:
        return self.__arr[pos]

    def _getItemFromValue(self, value: int | float | str) -> List[int, any | None]:
        """
        Retrieves the index of the item and the item itself based on a given value.
        :param value: The value to check inside the array list. The value could be a primitive value like 1, \"Name\", or \"1.02\".
        :return: The index of the item, and the item itself. Index will be -1 and item will be None 
            if the value is not found.
        """
        index = -1
        item = None
        # Check item
        for i in range(self._getSize()):
            if self._get(i) == value:
                index = i 
                item = self._get(i)
                break

        return [index, item]
    


    def _insert(self, item: any, pos: int = -1) -> bool:
        """
        Inserts a new item of the object type to the specified position. Defaults to insert at last.
        :param item: Item to be inserted.
        :param pos: Position to insert into. Must not exceed current number of elements of array list.
        :return: Flag if insertion was successful or not. May raise an error if assertion is incorrect.
        """
        assert self._checkDataType(item), "Incorrect data type of item given."
        assert pos < self._getSize(), "Invalid position."

        # Check if Array List is full
        if self.__size >= len(self.__arr):
            self.__increaseListSize()

        pos = self._getSize() if pos == -1 else pos

        self.__adjust(self._getSize(), pos, "f")

        self.__arr[pos] = item
        self.__increaseSize()
        return True

    @staticmethod
    def _setAdjustCondition(counter: int, sentinel: int, operator: str) -> bool:
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
        assert 0 <= start <= self._getSize(), "Start index out of bounds."
        assert 0 <= end <= self._getSize(), "End index out of bounds."

        d = d.lower()

        operator = ">=" if d == "f" else "<="

        while ArrayList._setAdjustCondition(start, end, operator):
            if d == "f":
                self.__arr[start] = self.__arr[start - 1]
                start -= 1
            else:
                self.__arr[start] = self.__arr[start + 1]
                start += 1

    def _update(self, value: any, pos: int) -> bool:
        """
        Updates the element at the index with a new element.
        :param value: New value to replace at index.
        :param pos: Index of element to be updated.
        :return: Flag if update was done or not.
        """
        assert 0 <= pos < self._getSize(), "Index of element out of bounds."
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

    def _remove(self, pos: int) -> any:
        """
        Removes an item from the position of this list.
        :param pos: Position of item to be removed. Must be within 0 and size of this array - 1.
        :return: The item that was removed.
        """
        assert isinstance(pos, int), "Invalid position type given."
        assert 0 <= pos < self._getSize(), "Removal index out of bounds."

        item = self._get(pos)
        self.__adjust(pos, self._getSize(), "b")
        self.__decreaseSize()
        return item

    def _removeOnValue(self, value: Callable | int | float | str) -> any:
        """
        Removes an item based on the given method to retrieve its value.
        :param value: Method to retrieve value from the array list, or can be an absolute value 
            such as integer, float, or string.
        :return: Item if it exists based on value. None if it does not.
        """
        assert isinstance(value, (Callable, int, float, str)), "Invalid data type of value given."

        target = None

        for i in range(self._getSize()):
            try:
                # Check if target is callable
                target = value()
            except:
                # If it is not callable, try setting as primitive value.
                target = value
            finally:
                if self._get(i) == target:
                    return self._remove(i)

        # If loop terminates, that means that the element with such value was not found.
        print("Item to be removed not found.")
        return None

    def _sort(self, comparator: Callable[[any, any], int], new_copy: bool = False) -> 'ArrayList':
        """
        Sorts this array list based on some comparison. May create a sorted copy or not. Utilizes selection sort.
        :param comparator: Comparison method used for sorting elements. The comparison method
            must always be in the form: compare(a, b,), and must return an int between the following: -1, 0, and 1.
        :param new_copy: Flag if this sort operation should produce a copy and not compromise the original array.
        :return:
        """
        l = ArrayList.deepcopy(self) if new_copy else self

        for i in range(0, l._getSize()):
            idx = i
            for j in range(i, l._getSize()):
                if comparator(l._get(j), l._get(idx)) < 0:
                    idx = j

            temp = l._get(i)
            l._update(l._get(idx), i)
            l._update(temp, idx)

        return l
    
    def deepcopy(source: 'ArrayList') -> 'ArrayList':
        """
            Creates a deep copy from one array list to the other array list.
        """
        arr = ArrayList(source._getDataType(), source._getSize())

        # Insert each item
        for i in range(source._getSize()):
            arr._insert(source._get(i))

        return arr


    def __str__(self) -> str:
        s = "[ "

        for i in range(self.getSize()):
            s += str(self._get(i))

            if (i + 1) < self.getSize():
                s += ", "

        s += " ]"

        return s