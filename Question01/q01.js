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
