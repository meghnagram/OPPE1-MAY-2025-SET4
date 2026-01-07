
def extract_email_username(email: str) -> str:
    '''
    Given an email address string of the form "username@domain.com", 
    return just the username part (everything before the @ symbol).

    Examples:
    >>> extract_email_username("ananya.sharma@iitd.ac.in")
    "ananya.sharma"
    >>> extract_email_username("rahul123@gmail.com")
    "rahul123"
    >>> extract_email_username("priya_r@company.in")
    "priya_r"
    >>> extract_email_username("v.kumar@institute.edu")
    "v.kumar"

    Args:
        email (str): A valid email address

    Returns:
        str: The username part of the email (before the @)
    '''
    
    return email.split('@')[0]

# #Another Method:


# def extract_email_username(email: str) -> str:
#     a=email.index("@")
#     return email[0:a:]

# Extract Email Username
# Write a function extract_email_username that takes an email address string of the form "username@domain.com" and returns just the username part — that is, everything before the @ symbol.

# Constraints

# The input will always be a valid email address containing exactly one @ symbol.
# The username can contain letters, numbers, and symbols like dots or underscores.
# The domain part is irrelevant and should not be returned.
# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> extract_email_username("ananya.sharma@iitd.ac.in")
# "ananya.sharma"
# >>> extract_email_username("rahul123@gmail.com")
# "rahul123"
# >>> extract_email_username("priya_r@company.in")
# "priya_r"
# >>> extract_email_username("v.kumar@institute.edu")
# "v.kumar"
    
