import re

def to_snake_case(input_string):
    """
    Convert a given string to snake_case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The converted snake_case string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not input_string:
        return ""
    
    # Handle camelCase and PascalCase by inserting underscores
    # before any uppercase letters that are preceded by a lowercase letter
    # or followed by a lowercase letter
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    
    # Convert to lowercase and replace non-alphanumeric characters with underscores
    snake_case = re.sub(r'[^a-z0-9]+', '_', s2.lower())
    
    # Remove leading and trailing underscores
    snake_case = snake_case.strip('_')
    
    return snake_case