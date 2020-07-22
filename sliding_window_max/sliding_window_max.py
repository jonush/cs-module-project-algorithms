'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# [[1 3 -1] -3 5 3 6 7]
# [1 [3 -1 -3] 5 3 6 7]
# [1 3 [-1 -3 5] 3 6 7]
# [1 3 -1 [-3 5 3] 6 7]
# [1 3 -1 -3 [5 3 6] 7]
# [1 3 -1 -3 5 [3 6 7]]
#
# slice of size 3
# window moves 1 element over each time
# return the max value in each window
# [n:n + k - 1] -> i = 0, k = 3
# [0:2]
# [1:3]
# [3:5]

# currently O(n²)
def sliding_window_max(nums, k):
    max_values = []

    for i in range(len(nums)):
        if len(nums[i:i + k]) == k:
            max_values.append(max(nums[i:i + k]))
    
    return max_values

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")