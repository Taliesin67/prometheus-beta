import re

def reverse_words_in_string(input_string):
    """
    Reverse the order of each word in the input string while maintaining 
    original capitalization and punctuation.
    
    Args:
        input_string (str): The input string to process
    
    Returns:
        str: A string with words reversed, preserving capitalization and punctuation
    """
    # Handle empty or None input
    if not input_string:
        return input_string
    
    def process_word(word):
        """
        Process a word: split alpha and non-alpha parts, reverse alpha part
        """
        # If no alphabetic characters, return as-is
        if not re.search(r'[a-zA-Z]', word):
            return word
        
        # Split into alpha and non-alpha parts
        parts = re.findall(r'[a-zA-Z]+|[^a-zA-Z]+', word)
        
        # Reverse only alphabetic parts while preserving case
        reversed_parts = []
        for part in parts:
            if part.isalpha():
                # Preserve original part's case
                if part.istitle():
                    reversed_part = part[::-1].capitalize()
                elif part.isupper():
                    reversed_part = part[::-1].upper()
                elif part.islower():
                    reversed_part = part[::-1].lower()
                else:
                    # Mixed case, just reverse as-is
                    reversed_part = part[::-1]
                reversed_parts.append(reversed_part)
            else:
                # Non-alphabetic parts stay the same
                reversed_parts.append(part)
        
        return ''.join(reversed_parts)
    
    # Use regex to split string into words and non-word elements
    tokens = re.findall(r'\b\w+\b|[^\w\s]+|\s+', input_string)
    
    # Process each token
    processed_tokens = [process_word(token) for token in tokens]
    
    return ''.join(processed_tokens)