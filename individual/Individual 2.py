#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    lis = []
    m, c, k = 1, 0, 0

    n = int(input('Введите количество чисел в списке: '))
    print('Введите числа в список: ')
    for i in range(n):
        lis.append(int(input()))
        if (i+1) % 2 == 0:
            m *= lis[i]

    # print(m)
    for i in lis:
        if i == 0:
            if k == 1:
                break
            k = 1
            continue
        if k == 1:
            c += i

    lis.sort(reverse=True)
    print("сумма между нулями", c, "произведение четных", m)
    print("преобразованный список", lis)
