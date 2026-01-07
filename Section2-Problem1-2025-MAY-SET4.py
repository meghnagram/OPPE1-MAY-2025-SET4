
def alternate_upper(sentence: str) -> list:
    """
    Given a sentence, return a list where every alternate word starting from the first is in uppercase.

    Example:
    alternate_upper("this is a test case")
    >>> ['THIS', 'is', 'A', 'test', 'CASE']

    Args:
        sentence (str): A single string containing words separated by spaces.

    Returns:
        list: A list of words with alternate words in uppercase.
    """
    
    
    words = sentence.split()
    result = [word.upper() if i % 2 == 0 else word for i, word in enumerate(words)]
    return result
    
# #Another Method

# def alternate_upper(sentence: str) -> list:
     
#     d=[]
#     d=sentence.split()
#     for i in range(len(d)):
#         if i%2==0:
#             d[i]=d[i].upper()
        
#     return(d)
        
# Upper Case Even Index Words
# Write a program that takes a sentence as input and returns a list of words where the words at even indices (0-based indexing) are converted to uppercase, while the others remain unchanged.

# The output must be printed as a list.

# Constraints:
# Words are separated by spaces.
# Keep all other formatting intact.
# Indexing starts at 0.
# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example
# Input

# india is my country
# Output

# ['INDIA', 'is', 'MY', 'country']

