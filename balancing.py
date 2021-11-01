from stack import Stack


def analize_balancing(string):
    """
    Функция, используя методы класса Stack, определяет сбалансированность скобок в строке.
    Если число элементов нечетное - скобки несбалансированы. Если четное: в худшем случае, за максимальное количество
    итераций, равное половине квадрата количества элементов, функция удалит попарно открывающую и закрывающую скобки
    (минимум одну пару за цикл). Если элементов не останется, количество и расположение скобок сбалансировано. Если цикл
    закончится, а в словаре что-то останентся - несбалансировано. Например, может остаться что-то вроде '([)]'.
    :param string: строка из скобок
    :return: 'Сбалансировано' или 'Несбалансировано'
    """
    main = list(string)
    temp = []

    if Stack.size(main) % 2 != 0:
        return 'Несбалансированно'
    for count in range(int(Stack.size(main) * Stack.size(main) / 2)):
        if not Stack.isEmpty(main):
            Stack.push(temp, Stack.pop(main))
        if not Stack.isEmpty(main) and not Stack.isEmpty(temp):
            if Stack.peek(temp) == '(' and Stack.peek(main) == ')' or \
                    Stack.peek(temp) == '[' and Stack.peek(main) == ']' or \
                    Stack.peek(temp) == '{' and Stack.peek(main) == '}':
                Stack.pop(temp)
                Stack.pop(main)
        if Stack.isEmpty(main) and Stack.isEmpty(temp):
            return 'Сбалансировано'
        if Stack.isEmpty(main) or Stack.isEmpty(temp):
            for n in range(Stack.size(temp)):
                Stack.push(main, Stack.pop(temp))
    return 'Несбалансированно'


if __name__ == '__main__':
    quotes = '[([])((([[[]]])))]{()}[]'
    print(analize_balancing(quotes))
