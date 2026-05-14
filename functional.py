from functools import reduce

def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0
    if isinstance(numbers[0],int):
        return numbers[0] + recursive_sum(numbers[1:])
    else:
        return recursive_sum(numbers[0])+ recursive_sum(numbers[1:])
    
# You can edit this code to try different testing cases.

assert recursive_sum([1, 2, [3, 4], [[5], 6], 7]) == 28
assert recursive_sum([1, [2, [3, [4, [5]]]]]) == 15
assert recursive_sum([]) == 0
assert recursive_sum([[[[[]]]]]) == 0
assert recursive_sum([10, [20, 30], 40, [50, [60]]]) == 210

def recursive_sum_reduce(numbers):
    print(f'Processing: {numbers=}')
    def helper(acc, val):
        if isinstance(val, int):
            return acc + val
        else:
            return acc + recursive_sum_reduce(val)
    return reduce(helper, numbers, 0)

assert recursive_sum_reduce([1, 2, [3, 4], [[5], 6], 7]) == 28
assert recursive_sum_reduce([1, [2, [3, [4, [5]]]]]) == 15
assert recursive_sum_reduce([]) == 0
assert recursive_sum_reduce([[[[[]]]]]) == 0
assert recursive_sum_reduce([10, [20, 30], 40, [50, [60]]]) == 210

