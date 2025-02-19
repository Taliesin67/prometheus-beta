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
        Precisely reverse a word while preserving its original characteristics
        """
        # First, separate alphabetic characters from non-alphabetic
        alpha_chars = [c for c in word if c.isalpha()]
        
        # If no alphabetic characters, return the word as-is
        if not alpha_chars:
            return word
        
        # Reverse the alphabetic characters 
        reversed_alpha = alpha_chars[::-1]
        
        # Reconstruct the word
        result = []
        alpha_index = 0
        for char in word:
            if char.isalpha():
                result.append(reversed_alpha[alpha_index])
                alpha_index += 1
            else:
                result.append(char)
        
        # Restore original case characteristics of the alpha parts 
        # This ensures the reversed chars have the right casing
        for i, char in enumerate(result):
            if char.isalpha():
                if word[i].isupper():
                    result[i] = char.upper()
                elif word[i].islower():
                    result[i] = char.lower()
        
        return ''.join(result)
    
    # Split the string while preserving tokens
    tokens = re.findall(r'\b[a-zA-Z0-9]+\b|[^\w\s]+|\s+', input_string)
    
    # Process tokens, reversing only word-like tokens 
    processed_tokens = [
        reverse_word(token) if re.match(r'\b[a-zA-Z0-9]+\b', token) else token 
        for token in tokens
    ]
    
    return ''.join(processed_tokens)