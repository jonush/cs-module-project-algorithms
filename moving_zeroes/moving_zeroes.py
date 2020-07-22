'''
Input: a List of integers
Returns: a List of integers
'''

# [0,2,0,0,3,0,6,0] -> [2,3,6,0,0,0,0,0]

# currently O(n)
def moving_zeroes(arr):
    # iterate through array
        # if value != 0, move to front of list
    for n in arr:
        if n != 0:
            arr.insert(0, arr.remove(n))

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")