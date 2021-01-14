from functools import reduce
from collections import deque


first_hex = list('11FFFFFF')  # input('Введите первое шестнадцатеричное число: ')
second_hex = list('F1203ABC')  # input('Введите второе шестнадцатеричное число: ')


def hex_sum(a, b):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    a = list.copy(a)
    b = list.copy(b)
    if len(a) < len(b):
        a, b = b, a
    k_sum = 0
    res_sum = deque([])

    for i in range(len(a)):
        first = a.pop() if a else '0'
        second = b.pop() if b else '0'
        sum_f_s = numbers.index(first) + numbers.index(second) + k_sum

        if sum_f_s > 15:
            res_sum.appendleft(numbers[sum_f_s % 16])
            k_sum = sum_f_s // 16
            if not a:
                res_sum.appendleft(numbers[k_sum])
        if sum_f_s <= 15:
            res_sum.appendleft(numbers[sum_f_s])
            k_sum = 0
    return list(res_sum)


def hex_multiplication(a, b):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    a = list.copy(a)
    c = list.copy(b)

    res_mpl = deque([])

    for i in range(len(a)):
        b = list.copy(c)
        first = a.pop()
        temp = deque([])
        k_mpl = 0

        for j in range(len(b)):
            second = b.pop()
            multiplication_f_s = numbers.index(first) * numbers.index(second) + k_mpl

            if multiplication_f_s > 15:
                temp.appendleft(numbers[multiplication_f_s % 16])
                k_mpl = multiplication_f_s // 16
                if not b:
                    temp.appendleft(numbers[k_mpl])

            if multiplication_f_s <= 15:
                temp.appendleft(numbers[multiplication_f_s])
                k_mpl = 0

        if i > 0:
            for k in range(i):
                temp.append('0')

        res_mpl.appendleft(list(temp))

    summ_mpl = reduce(hex_sum, res_mpl)

    return summ_mpl


print(hex_sum(first_hex, second_hex))
print(hex_multiplication(first_hex, second_hex))
