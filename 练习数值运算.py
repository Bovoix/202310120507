def max_subarray_sum(nums):
    if not nums:
        return 0
    current_max = global_max = nums[0]
    for num in nums[1:]:
        current_max = max(num, current_max + num)
        if current_max > global_max:
            global_max = current_max
    
    return global_max
if __name__ == "__main__":
    test_cases = [
        [1, -2, 3, 5, -1],    
        [1, -2, 3, -8, 5, 1], 
        [1, -2, 3, -2, 5, 1]  
    ]
    
    for i, arr in enumerate(test_cases):
        result = max_subarray_sum(arr)
        print(f"测试用例 {i+1}: {arr}")
        print(f"子数组之和的最大值: {result}\n")
    