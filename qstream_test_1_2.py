# -*- coding: utf-8 -*-
"""Qstream_TestTest.ipynb


1.   Q) Write a method that given an array of integers and an integer target, and returns an array of the two indexes of the elements that add up to the target.

    e.g. ([1, 2, 3, 7], 8) → [0,3]
  
  The same element cannot be used twice, you may assume all integers are positive and for each input
there is only one solution.
"""

def sum_two(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return None

# Test the function for Q1
nums = [1, 2, 3, 7,]
target = 8
sum_two(nums, target)


"""2.   Q) Write a method that given an array of arbitrarily nested arrays, flattens the input and
returns it.

  e.g. flatten([[0, 1, [3]], [5, [7]]]) → [0,1,3,5,7]

  Solutions that use Ruby’s Array#flatten or similar in other languages will not be accepted.
"""

def flatten_nested_array(nests):
    flattened = []
    for item in nests:
        if isinstance(item, list):
            flattened.extend(flatten_nested_array(item))
        else:
            flattened.append(item)
    return flattened

# Test the function
nested_array = [[[0, 1, [3]], [5, [7]]]]
print(flatten_nested_array(nested_array))