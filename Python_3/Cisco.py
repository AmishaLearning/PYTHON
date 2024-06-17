def find_max_elements(array):
    target = sum(array) // 2  # Target is half the sum of the array elements
    memo = {}

    def backtrack(index, curr_sum):
        if index == len(array) or curr_sum > target:
            return 0
        if (index, curr_sum) in memo:
            return memo[(index, curr_sum)]

        include = 0
        if curr_sum + array[index] <= target:
            include = 1 + backtrack(index + 1, curr_sum + array[index])

        exclude = backtrack(index + 1, curr_sum)

        memo[(index, curr_sum)] = max(include, exclude)
        return memo[(index, curr_sum)]

    return backtrack(0, 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    array_count = int(input().strip())

    array = []

    for _ in range(array_count):
        array_item = int(input().strip())
        array.append(array_item)

    result = find_max_elements(array)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
    
#!/bin/python3

import math
import os
import random
import re
import sys



def find_max_apples(max_size_difference, apple_sizes):
    apple_sizes.sort()  # Sort the apple sizes in ascending order
    start = 0
    max_apples = 0

    for end in range(len(apple_sizes)):
        while apple_sizes[end] - apple_sizes[start] > max_size_difference:
            start += 1

        max_apples = max(max_apples, end - start + 1)

    return max_apples
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    max_size_difference = int(input().strip())

    apple_sizes_count = int(input().strip())

    apple_sizes = []

    for _ in range(apple_sizes_count):
        apple_sizes_item = int(input().strip())
        apple_sizes.append(apple_sizes_item)

    result = find_max_apples(max_size_difference, apple_sizes)

    fptr.write(str(result) + '\n')

    fptr.close()

    
    
    
