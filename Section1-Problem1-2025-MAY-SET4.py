
def double_ends(l: list) -> list:
    '''
    Given a list with at least two elements, return a new list where:
    - the first element is duplicated at the beginning
    - the last element is duplicated at the end

    The original list should remain unchanged.

    Examples:
    >>> double_ends([10, 20, 30])
    [10, 10, 20, 30, 30]
    >>> double_ends(['a', 'b', 'c'])
    ['a', 'a', 'b', 'c', 'c']
    >>> double_ends([1, 2])
    [1, 1, 2, 2]
    >>> double_ends([5, 6, 7, 8])
    [5, 5, 6, 7, 8, 8]

    Args:
        l (list): A list with at least two elements

    Returns:
        list: A new list with first and last elements duplicated
    '''
    
    return [l[0]] + l + [l[-1]]


# Double First and Last Elements in a List
# Write a function double_ends(l) that takes a list l (with at least two elements) and returns a new list where the first and last elements of l are duplicated at the beginning and end of the list, respectively.

# The new list should have:

# The first element of the original list inserted once at the beginning
# The last element of the original list inserted once at the end
# You must not modify the original list.

# Constraints

# The input list will contain at least two elements
# The list can contain elements of any type (integers, strings, etc.)
# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> double_ends([10, 20, 30])
# [10, 10, 20, 30, 30]
# >>> double_ends(['a', 'b', 'c'])
# ['a', 'a', 'b', 'c', 'c']
# >>> double_ends([1, 2])
# [1, 1, 2, 2]
# >>> double_ends([5, 6, 7, 8])
# [5, 5, 6, 7, 8, 8]

