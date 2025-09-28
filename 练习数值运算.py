def max_subarray_sum(nums):
    # 处理空数组的情况
    if not nums:
        return 0
    
    # 初始化当前最大和与全局最大和为数组的第一个元素
    current_max = global_max = nums[0]
    
    # 从数组的第二个元素开始遍历
    for num in nums[1:]:
        # 对于每个元素，判断是加入当前子数组还是开始新的子数组
        current_max = max(num, current_max + num)
        # 更新全局最大和
        if current_max > global_max:
            global_max = current_max
    
    return global_max

# 测试示例
if __name__ == "__main__":
    test_cases = [
        [1, -2, 3, 5, -1],    # 预期输出: 8
        [1, -2, 3, -8, 5, 1], # 预期输出: 6
        [1, -2, 3, -2, 5, 1]  # 预期输出: 7
    ]
    
    for i, arr in enumerate(test_cases):
        result = max_subarray_sum(arr)
        print(f"测试用例 {i+1}: {arr}")
        print(f"子数组之和的最大值: {result}\n")
    