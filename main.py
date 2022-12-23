# Возвращает результат математической операции "text[1]" с числами "text[0]" и "text[2]"
# Входные данные - числа "text[0]" и "text[2]" и знак математической операции "sign"
# Граничные значения:
#   text[0], text[2] - числа
#   text[1] - знак из множества "+, -, *, /"
# Возвращает результат математической операции
def calc(text):
    result = 0
    if text[1] == '+':
        result = int(text[0]) + int(text[2])
    elif text[1] == '-':
        result = int(text[0]) - int(text[2])
    elif text[1] == '*':
        result = int(text[0]) * int(text[2])
    elif text[1] == '/':
        result = int(text[0]) / int(text[2])
    else:
        print("error")
    # print(result)
    return result

# Сортирует список "a" по возрастанию
# Входные данные - натуральное число "n"
# Граничные значения:
#   a - список чисел
# Возвращает отсортированный по возрастанию список "a"
def bubblesort(a : list):
    N = len(a)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Вывод списка из "n" чисел Фибоначчи
# Входные данные - натуральное число "n"
# Граничные значения:
#   a - натуральное число
# Возвращает "n" чисел Фибоначчи
def fib(n):
    arr = []
    arr.append(1)
    arr.append(1)

    fib1 = fib2 = 1

    n = int(n) - 2

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
        arr.append(fib2)
    # print(arr)
    return arr

def main():
    print(fib(10))
    print(bubblesort([1, 5, 3, 2, 4]))
    print(calc("5*3"))


if __name__ == '__main__':
    main()
