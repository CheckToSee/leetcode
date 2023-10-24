class DynamicArray:

    def __init__(self, capacity: int):
        return [None] * capacity

    def get(self, i: int) -> int:
        return self[i]

    def set(self, i: int, n: int) -> None:
        self[i] = n

    def pushback(self, n: int) -> None:
        return

    def popback(self) -> int:
        return

    def resize(self) -> None:
        return

    def getSize(self) -> int:
        return

    def getCapacity(self) -> int:
        return
