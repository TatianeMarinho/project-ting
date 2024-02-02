from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return not self.__len__()

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Vazio')
        return self._data.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]
