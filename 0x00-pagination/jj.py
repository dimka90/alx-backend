#!/usr/bin/env python3

"""
This program takes in a list of numbers and return there sum
"""

from typing import List


def sum_list(input_list: List[float]) -> float:

    sum: float = 0.0
    for i in input_list:
        sum = sum + i
    return sum


print(sum_list([90,90,900]))