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
    
    def reverse_word(word):
        """
        Reverse a word while preserving its original case and structure
        """
        if not word.isalpha():
            return word
        
        # Reverse the word itself
        reversed_word = word[::-1]
        
        # Restore original capitalization
        if word.istitle():
            reversed_word = reversed_word.capitalize()
        elif word.isupper():
            reversed_word = reversed_word.upper()
        elif word.islower():
            reversed_word = reversed_word.lower()
        
        return reversed_word
    
    def process_alphanumeric(word):
        """
        Handle alphanumeric words with special preservation
        """
        # If word is purely alphabetic, use reverse_word
        if word.isalpha():
            return reverse_word(word)
        
        # If word contains numbers, try to preserve original numeric parts
        alpha_part = ''.join(c for c in word if c.isalpha())
        numeric_part = ''.join(c for c in word if c.isdigit())
        
        # Reverse alpha part while preserving case
        reversed_alpha = reverse_word(alpha_part)
        
        # Reconstruct the word
        if word.isalnum():
            return reversed_alpha + numeric_part[::-1]
        
        return word
    
    # Tokenize the string, preserving all elements
    pattern = re.compile(r'(\b[a-zA-Z0-9]+\b|[^\sa-zA-Z0-9]+|\s+)')
    tokens = pattern.findall(input_string)
    
    # Process tokens
    processed_tokens = [
        process_alphanumeric(token) if re.match(r'\b[a-zA-Z0-9]+\b', token) else token 
        for token in tokens
    ]
    
    return ''.join(processed_tokens)