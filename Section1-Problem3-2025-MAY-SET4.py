
def shuffle_digits(num: int) -> int:
    '''Returns the number with digits shuffled in order 2413.

    Examples:
    >>> shuffle_digits(1234)
    2413
    >>> shuffle_digits(2413)
    4321
    >>> shuffle_digits(4321)
    3142
    >>> shuffle_digits(3142)
    1234

    Args:
        num (int): A 4-digit positive integer

    Returns:
        int: digit shuffled integer.
    '''
    
    
    s = str(num)
    return int(s[1]+s[3]+s[0]+s[2])
    
# #Another Method:
# def shuffle_digits(num: int) -> int:
    
#     s=str(num)
#     a=s[1]+s[3]+s[0]+s[2]
    
#     return int(a)

# Four Digit Shuffle
# Write a function shuffle_digits(num) that takes a 4-digit positive integer and shuffles the digits in the order 2413. That is

# The 2nd digit from left becomes the 1st
# The 4th digit from left becomes the 2nd
# The 1st digit from left becomes the 3rd
# The 3rd digit from left becomes the 4th
# Example

# >>> shuffle_digits(1234)
# 2413
# >>> shuffle_digits(2413)
# 4321
# >>> shuffle_digits(4321)
# 3142
# >>> shuffle_digits(3142)
# 1234
