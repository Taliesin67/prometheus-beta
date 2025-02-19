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
    
    # Helper function to reverse a word while maintaining its case
    def reverse_and_match_case(word, original):
        # If the input is not a pure alphabetic word, return as-is
        if not word.replace('-', '').isalpha():
            return word
        
        # Reverse the word
        reversed_word = word[::-1]
        
        # Restore original capitalization 
        if original.istitle():
            reversed_word = reversed_word.capitalize()
        elif original.isupper():
            reversed_word = reversed_word.upper()
        elif original.islower():
            reversed_word = reversed_word.lower()
        
        # Special handling for alphanumeric words
        if any(c.isdigit() for c in original):
            # If original word contained digits, ensure digits are preserved
            reversed_word = ''.join(
                d if not c.isalpha() else c 
                for c, d in zip(original, reversed_word + original)
            )
        
        return reversed_word
    
    # Split the string into meaningful tokens
    def tokenize(s):
        # This regex captures words, numbers, punctuation, and whitespace
        return re.findall(r'[a-zA-Z0-9]+|[^\sa-zA-Z0-9]+|\s+', s)
    
    # Tokenize and process
    tokens = tokenize(input_string)
    
    # Reverse only alphabetic/alphanumeric tokens
    reversed_tokens = [
        reverse_and_match_case(token, token) if token.replace('-', '').isalpha() else token 
        for token in tokens
    ]
    
    return ''.join(reversed_tokens)