from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    closest_sum = float('inf')
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            
            # If this sum is closer, update
            if abs(target - curr_sum) < abs(target - closest_sum):
                closest_sum = curr_sum
            
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return curr_sum  # Exact match
    
    return closest_sum


# 🔹 Testing
print(threeSumClosest([-1,2,1,-4], 1))  # Output: 2
print(threeSumClosest([0,0,0], 1))      # Output: 0
