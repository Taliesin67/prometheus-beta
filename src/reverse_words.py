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
    def reverse_word(word):
        if not word.replace('-', '').isalpha():
            return word
        
        # Reverse the word
        reversed_word = word[::-1]
        
        # Restore original capitalization
        if word.istitle():
            reversed_word = reversed_word.capitalize()
        elif word.isupper():
            reversed_word = reversed_word.upper()
        elif word.islower():
            reversed_word = reversed_word.lower()
        
        return reversed_word
    
    # Split the string into words and non-word tokens
    tokens = re.findall(r'\w+|[^\w\s]|\s+', input_string)
    
    # Reverse only the words
    reversed_tokens = [reverse_word(token) if token.replace('-', '').isalpha() else token for token in tokens]
    
    return ''.join(reversed_tokens)