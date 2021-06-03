# Find factorial of a large number

import sys

# This function finds factorial of a large number and prints them
def factorial(n):
    res = [None]*500
    # Initialize result
    res[0] = 1
    res_size = 1

    # Apply simple factorial formula
    # n!= 1 * 2 * 3 * ... * n
    x = 2
    while x <= n:
        res_size = multiply(x, res, res_size)
        x = x + 1

    print("Factorial of given number is:")
    i = res_size - 1
    while i >= 0:
        print(str(res[i]))
        i = i - 1



# This function multiplies x with the number represented by res[]. res_size is size of res[] or number of digits in the number
# res_size is size of res[] or number of digits in the number represented by res[]. 
# This function uses simple school mathematics for multiplication. This function may value of res_size and returns the new value of res_size
def multiply(x, res, res_size):

    carry = 0       # Initialize carry
    # One by one multiply n with individual digits of res[]
    i = 0
    while i < res_size:
        prod = res[i] * x + carry
        res[i] = prod % 10          # Store last digit of 'prod' in res[]
        # Make sure floor division is used
        carry = prod // 10
        i = i + 1

    # Put carry in res and increase result size
    while carry:
        res[res_size] = carry % 10
        # Make sure floor division is used to avoid floating value
        carry = carry // 10
        res_size = res_size + 1

    return res_size




# Driver Program
factorial(100)