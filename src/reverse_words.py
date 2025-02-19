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
    
    # Split the string, preserving whitespace and punctuation
    def split_with_spaces(s):
        # Uses regex to split while keeping delimiters
        return re.findall(r'\s+|\W+|\w+', s)
    
    # Reverse each word while maintaining its original case
    def reverse_word(word):
        if not word.isalpha():
            return word
        
        # Determine the original case of the word
        if word.istitle():
            return word[::-1].capitalize()
        elif word.isupper():
            return word[::-1].upper()
        elif word.islower():
            return word[::-1].lower()
        else:
            return word[::-1]
    
    # Split the string and process each token
    tokens = split_with_spaces(input_string)
    reversed_tokens = [reverse_word(token) if token.isalpha() else token for token in tokens]
    
    return ''.join(reversed_tokens)