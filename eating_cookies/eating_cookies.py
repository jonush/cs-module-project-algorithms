'''
Input: an integer
Returns: an integer
'''

# currently
def eating_cookies(n):
    # how many combinations of cookie eating are possible when given n amount of cookies?
    # can eat 1, 2, or 3 cookies at a time
    # if there are 0 cookies left, cannot eat anymore
    #
    # if using recursion, what is the base case?
    # if there are no more cookies left, that method of eating cookies is finished

    # base case
    # there are no more cookies to eat
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
 
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
