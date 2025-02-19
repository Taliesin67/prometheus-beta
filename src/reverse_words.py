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
        # If word contains non-alphabetic characters, return as-is
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
    
    # Split the string preserving tokens and whitespace
    # Captures words, punctuation, and whitespace
    tokens = re.findall(r'\b[a-zA-Z]+\b|[^\sa-zA-Z]+|\s+', input_string)
    
    # Process and reverse words
    reversed_tokens = [process_word(token) if re.match(r'\b[a-zA-Z]+\b', token) else token for token in tokens]
    
    return ''.join(reversed_tokens)