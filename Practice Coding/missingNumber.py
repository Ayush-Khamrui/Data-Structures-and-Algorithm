# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
 

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?


################################################################################################################## 
# Answer ----> BruteForce
# -----------------------
# let's take for example nums list having [3,0,1]
# So the only number missing here is 4 
# Now we can do one thing
# Step 1 - Sort the list
# Step 2 - iterate over the list then find the missing number

# This will have a time Complexity of nlog(n)

# Optimized Approach 
# --------------------------
# We can use XOR in this case because XOR of two similar number is 0
# and XOR of a number with 0 is the very same number
# like 5^5 = 0
# 5^6^5 = 6
# 0^5 = 5

# So the time complexity of this approach is O(n)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorValue = 0
        for i in range(len(nums)+1):
            xorValue = xorValue^i
        for i in nums:
            xorValue = xorValue^i
        return xorValue
