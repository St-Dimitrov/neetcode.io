def productExceptSelf(self, nums: List[int]) -> List[int]:
    zero_count = nums.count(0)
    total_product = 1
    for num in nums:
        if num != 0:
            total_product *= num
    result = []
    for num in nums:
        if zero_count == 0:
            result.append(total_product // num)
        elif zero_count == 1:
            result.append(total_product if num == 0 else 0)
        else:
            result.append(0)
    return result
