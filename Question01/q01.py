# Question: Given an array of integers, return the indices of the two numbers that add up to a given target.

def sum_two_component(nums, target):
    # Check nums
    if len(nums) < 2:
        return None
    # Have two pointers P1 and P2
    # Loop P1 from index of 0 to index of length-1
    for p1_index, p1 in enumerate(nums):
        # At each looping step of P1, calculate target value - P1's value to have the targeted number of P2.
        target_p2 = target - p1

        # Loop P2 from P1's index + 1, to the end. Compare value of P2 with the calculated value
        for p2_index in range(p1_index+1, len(nums)):
            if nums[p2_index] == target_p2:
                return [p1_index, p2_index]

    return None


def sum_two(nums, target):
    # Check nums
    if len(nums) < 2:
        return None

    # Generate nums_map with key is the num_to_find corresponding to
    # each index and value is index
    nums_map = {}

    # Loop P1 from index of 0 to index of length-1 of nums
    for index, value in enumerate(nums):
        if nums_map.get(value, None) is None:
            num_to_find = target - value
            nums_map.update({num_to_find: index})
        else:
            return [nums_map[value], index]

    return None


# test_array = [1, 3, 7, 9, 2]
# target = 11
# result = sum_two_component(test_array, target)
# print(result)  # Expect [3,4]
# result1 = sum_two(test_array, target)
# print(result1)  # Expect [3,4]

# test_array = [1, 3, 7, 9, 2]
# target = 25
# result = sum_two_component(test_array, target)
# print(result)  # Expect None
# result1 = sum_two(test_array, target)
# print(result1)  # Expect None

# test_array = []
# target = 4
# result = sum_two_component(test_array, target)
# print(result)  # Expect None
# result1 = sum_two(test_array, target)
# print(result1)  # Expect None

# test_array = [5]
# target = 5
# result = sum_two_component(test_array, target)
# print(result)  # Expect None
# result1 = sum_two(test_array, target)
# print(result1)  # Expect None

test_array = [1, 6]
target = 7
result = sum_two_component(test_array, target)
print(result)  # Expect [0,1]
result1 = sum_two(test_array, target)
print(result1)  # Expect [0,1]
