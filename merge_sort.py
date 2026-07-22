def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = 0  # Pointer for the left list
    j = 0  # Pointer for the right list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums
    
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]
    sorted_left_side = merge_sort(left_half)
    sorted_right_side = merge_sort(right_half)
    
    return merge(sorted_left_side, sorted_right_side)
