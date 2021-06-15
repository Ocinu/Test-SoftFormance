"""
Write a program that takes 4 inputs, where each input consists of 2 numbers in the format x,y. You are required to print a two-dimensional array having x rows and y columns for each input. The elements of the arrays should be whole numbers starting from 1 and incrementing by 1.

Example

Suppose the following 4 inputs are given to the program:

2,2
2,3
3,3
3,4

Then, the output of the program should be:

[[1, 2], [3, 4]]
[[1, 2, 3], [4, 5, 6]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

Note: You should assume that input to the program is from console input (raw_input)

"""
import numpy


def result(data: list):
    for i in data:
        i = i.split(',')
        array = numpy.arange(1, (int(i[0]) * int(i[1])+1))
        print(array.reshape(int(i[0]), int(i[1])))


"""
Alternative solution via list comprehension:

def gen_range_sublists(amount_sub_arr: int, amount_elems_sub_arr: int) -> list:
    return [[i for i in range(1, x * amount_elems_sub_arr + 1)][-amount_elems_sub_arr:] for x in
            range(1, amount_sub_arr + 1)]
"""


if __name__ == '__main__':
    parameter_list = [input(f'Enter {x + 1} pair of numbers: ') for x in range(4)]
    result(parameter_list)
