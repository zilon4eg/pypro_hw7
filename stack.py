class Stack:
    """
    isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека.
    peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    size - возвращает количество элементов в стеке.
    """
    @staticmethod
    def isEmpty(data):
        if data:
            return False
        else:
            return True

    @staticmethod
    def push(data, element):
        data.insert(0, element)
        return data

    @staticmethod
    def pop(data):
        result = data.pop(0)
        return result

    @staticmethod
    def peek(data):
        return data[0]

    @staticmethod
    def size(data):
        return int(len(data))
