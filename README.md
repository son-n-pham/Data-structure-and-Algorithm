# Data-structure-and-Algorithm

## How to approach the problem

Example question: Given an array of integers, return the indices of the two numbers that add up to a given target.
- After read the question very carefully, move on to the below step
- Step 1: Verify the constraints
  - Are there duplicate numbers in the array? Example answer: No, there is no duplicate
  - Will there always be a solution available? Example answer: No there may not always be a solution (empty array, array with 1 component, no 2 numbers to be added up to the given target)
  - What do we return if there's no solution? Example answer: Just return null.
  - Can there be multiple pairs that add up to the target? No, only 1 pair
- Step 2: Write out some test cases to cover the identified constraint
  - [1,3,7,9,2]  t=11  =>  [3,4]
  - [1,3,7,9,2]  t=25  =>  null
  - []           t=4   =>  null
  - [5]          t=5   =>  null
  - [1,6]        t=7   =>  [0,1]
- Step 3: Figure out a solution without code
  - Have two pointers P1 and P2
  - Loop P1 from index of 0 to index of length-1
    - At each looping step of P1, calculate target value - P1's value to have the targeted number of P2.
    - Loop P2 from P1's index + 1, to the end. Compare value of P2 with the calculated value
- Step 4: Put into code
```python
# Question: Given an array of integers, return the indices of the two numbers that add up to a given target.

def sum_two_component(input_array, target_value):
    # Check input_array
    if len(input_array) < 2:
        return None
    # Have two pointers P1 and P2
    # Loop P1 from index of 0 to index of length-1
    for p1_index, p1 in enumerate(input_array):
        # At each looping step of P1, calculate target value - P1's value to have the targeted number of P2.
        target_p2 = target_value - p1

        # Loop P2 from P1's index + 1, to the end. Compare value of P2 with the calculated value
        for p2_index in range(p1_index+1, len(input_array)):
            if input_array[p2_index] == target_p2:
                return [p1_index, p2_index]

    return None

test_array = [1, 3, 7, 9, 2]
target_value = 11
result = sum_two_component(test_array, target_value)
print(result) # Expect [3,4]

test_array = [1, 3, 7, 9, 2]
target_value = 25
result = sum_two_component(test_array, target_value)
print(result) # Expect None

test_array = []
target_value = 4
result = sum_two_component(test_array, target_value)
print(result) # Expect None

test_array = [5]
target_value = 5
result = sum_two_component(test_array, target_value)
print(result) # Expect None

test_array = [1, 6]
target_value = 7
result = sum_two_component(test_array, target_value)
print(result) # Expect [0,1]

```

- Step 5 (Optional): Optimization
  - The above solution is O(N<sup>2</sup>)
  - Hash map is a better solution
  - This solution uses O(N) space and O(N) time

```python
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
```

- Step 6 (My step to practice JS): Codes in JS :)

```javascript
'strict mode';

const sum_two = (nums, target) => {
  if (nums.length < 2) return null;

  for (let p1_index = 0; p1_index < nums.length; p1_index++) {
    numToFind = target - nums[p1_index];
    for (let p2_index = p1_index + 1; p2_index < nums.length; p2_index++) {
      if (nums[p2_index] === numToFind) return [p1_index, p2_index];
    }
  }

  return null;
};

const sum_two_map = (nums, target) => {
  if (nums.length < 2) return null;

  const nums_map = {};
  for (let i = 0; i < nums.length; i++) {
    numToFind = target - nums[i];

    if (nums_map[nums[i]]) {
      return [nums_map[nums[i]], i];
      // return 'hello';
    } else {
      nums_map[numToFind] = i;
    }
  }
  return null;
};

let test_array = [1, 3, 7, 9, 2];
let target_value = 11;
console.log(sum_two(test_array, target_value));
console.log(sum_two_map(test_array, target_value));
```
