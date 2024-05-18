# -*- coding: utf-8 -*-

import random
from typing import List, Tuple


def reduce_numbers(numbers: List[int], express: List[str], i: int, j: int) -> Tuple[List[int], List[str]]:
    new_arrays, new_express = [], []

    for ind in range(len(numbers)):
        if ind == i or ind == j:
            continue
        new_arrays.append(numbers[ind])
        new_express.append(express[ind])
    return new_arrays, new_express


def calculate(numbers: List[int], express: List[str]) -> str:
    """
    我有4个数字：[1 6 7 8]，如何对这四个数字进行加减乘除的运算组合得到24，并且要求每个数字只能用一次，给出一个组合方式
    :param numbers: 输入的数字列表
    :param express: 输入的表达式列表
    :return: 返回结果
    """

    if len(numbers) == 1 and numbers[0]==24:
        return express[0]

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            # 加法运算
            temp = numbers[i] + numbers[j]
            new_numbers, new_express = reduce_numbers(numbers, express, i, j)
            new_numbers.append(temp)
            new_express.append(f"({express[i]}+{express[j]})")
            result = calculate(new_numbers, new_express)
            if result != "":
                return result

            # 减法运算
            temp = numbers[i] - numbers[j]
            new_numbers, new_express = reduce_numbers(numbers, express, i, j)
            new_numbers.append(temp)
            new_express.append(f"({express[i]}-{express[j]})")
            result = calculate(new_numbers, new_express)
            if result != "":
                return result

            # 减法运算，交换两个数的位置
            temp = numbers[j] - numbers[i]
            new_numbers, new_express = reduce_numbers(numbers, express, i, j)
            new_numbers.append(temp)
            new_express.append(f"({express[j]}-{express[i]})")
            result = calculate(new_numbers, new_express)
            if result != "":
                return result

            # 乘法运算
            temp = numbers[i] * numbers[j]
            new_numbers, new_express = reduce_numbers(numbers, express, i, j)
            new_numbers.append(temp)
            new_express.append(f"({express[i]}*{express[j]})")
            result = calculate(new_numbers, new_express)
            if result != "":
                return result

            # 除法运算
            if numbers[j] != 0:
                temp = numbers[i] / numbers[j]
                new_numbers, new_express = reduce_numbers(numbers, express, i, j)
                new_numbers.append(temp)
                new_express.append(f"({express[i]}/{express[j]})")
                result = calculate(new_numbers, new_express)
                if result != "":
                    return result

            if numbers[i] != 0:
                temp = numbers[j] / numbers[i]
                new_numbers, new_express = reduce_numbers(numbers, express, i, j)
                new_numbers.append(temp)
                new_express.append(f"({express[j]}/{express[i]})")
                result = calculate(new_numbers, new_express)
                if result != "":
                    return result

    return ""


def main():
    """
    在终端输入4个数字
    :return:
    """
    while True:
        inputs = input("请输入4个数字，用空格隔开：")
        if inputs == "exit":
            break
        numbers = [int(x) for x in inputs.split()]
        random.shuffle(numbers)
        express = [str(x) for x in numbers]

        result = calculate(numbers, express)
        print("计算结果：", result)

if __name__ == '__main__':
    main()
