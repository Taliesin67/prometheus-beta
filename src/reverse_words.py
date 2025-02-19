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
        Reverse a word while preserving its original case
        """
        if not word.replace('-', '').isalpha():
            return word
        
        # Reverse the character sequence
        reversed_word = word[::-1]
        
        # Preserve original case characteristics
        if word.istitle():
            reversed_word = reversed_word.capitalize()
        elif word.isupper():
            reversed_word = reversed_word.upper()
        elif word.islower():
            reversed_word = reversed_word.lower()
        
        return reversed_word
    
    # Use a regex that preserves the original string structure
    # Captures words, punctuation, and whitespace
    tokens = re.findall(r'\b[a-zA-Z]+\b|[^\sa-zA-Z]+|\s+', input_string)
    
    # Reverse only the full alphabetic words
    reversed_tokens = [
        reverse_word(token) if re.match(r'\b[a-zA-Z]+\b', token) else token 
        for token in tokens
    ]
    
    return ''.join(reversed_tokens)