# /Problem Statement: Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = find_square_num(slow)
        fast = find_square_num(find_square_num(fast))
        if slow == fast:
            break
    return True


def find_square_num(num):
    _sum = 0
    while(num > 0):
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


print(find_happy_number(23))