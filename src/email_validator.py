import re

def validate_email(email: str) -> bool:
    """
    Validate the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.

    Validates email format based on RFC 5322 standard with some practical constraints:
    - Must have a local part (before @)
    - Must have a domain part (after @)
    - Local part can contain letters, digits, and some special characters
    - Domain must have at least one dot
    - Total length constraints
    """
    # Check if email is a string and not empty
    if not isinstance(email, str) or not email:
        return False

    # Check total email length
    if len(email) > 254:
        return False

    # Regular expression for email validation
    # Follows RFC 5322 standard with some practical constraints
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Additional checks
    try:
        # Check if email matches the regex pattern
        if not re.match(email_regex, email):
            return False
        
        # Split email into local and domain parts
        local_part, domain_part = email.rsplit('@', 1)
        
        # Check length constraints
        if len(local_part) > 64 or len(domain_part) > 253:
            return False
        
        return True
    
    except Exception:
        return False