def bubble_sort(nums: list[int]) -> list[int]:
    swap = True
    end = len(nums)
    while swap == True:
        swap = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i]= nums[i], nums[i-1]
                swap = True
        # -1 index from the end of the list 
        end -=1
    return nums