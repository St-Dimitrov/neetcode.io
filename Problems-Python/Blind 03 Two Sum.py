def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        print(num_map)
        # Calculate the difference needed to reach the target
        difference = target - num
        # Check if the difference is already in the hash map
        if difference in num_map:
            return [num_map[difference], i]
        num_map[num] = i
