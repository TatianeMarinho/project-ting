from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = []

    def __len__(self):
        return len(self.__data)

    def is_empty(self):
        return not self.__len__()

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Vazio')
        return self.__data.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.__data[index]
