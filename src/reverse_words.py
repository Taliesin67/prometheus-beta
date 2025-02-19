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
    
    def apply_original_case(reversed_word, original_word):
        """
        Apply the original word's case to the reversed word
        """
        if original_word.istitle():
            return reversed_word.capitalize()
        elif original_word.isupper():
            return reversed_word.upper()
        elif original_word.islower():
            return reversed_word.lower()
        return reversed_word
    
    def extract_alpha_and_numeric(word):
        """
        Separate alphabetic and numeric parts of a word
        """
        # Split into alpha and numeric segments
        alpha_part = ''.join(c for c in word if c.isalpha())
        numeric_part = ''.join(c for c in word if c.isdigit())
        return alpha_part, numeric_part
    
    def reverse_word(word):
        """
        Reverse a word while preserving its original characteristics
        """
        # If no alphabetic characters, return as-is
        if not any(c.isalpha() for c in word):
            return word
        
        # Extract alpha and numeric parts
        alpha_part, numeric_part = extract_alpha_and_numeric(word)
        
        # Reverse the alpha part
        reversed_alpha = apply_original_case(alpha_part[::-1], alpha_part)
        
        # Reconstruct the word, potentially with digits 
        if numeric_part:
            return reversed_alpha + numeric_part[::-1]
        return reversed_alpha
    
    # Split the string, preserving words and non-word tokens
    tokens = re.findall(r'\w+|[^\w\s]+|\s+', input_string)
    
    # Process tokens: only reverse tokens that are words
    processed_tokens = [
        reverse_word(token) if re.match(r'^[a-zA-Z0-9]+$', token) else token 
        for token in tokens
    ]
    
    return ''.join(processed_tokens)