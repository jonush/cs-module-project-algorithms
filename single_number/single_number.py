'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# currently O(n)
def single_number(arr):
    # track which integer shows up only once
    for n in arr:
        if arr.count(n) == 1:
            return n

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")