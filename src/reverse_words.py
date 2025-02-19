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
        Reverse only the alphabetic characters while maintaining case
        """
        # Separate alphabetic and non-alphabetic parts
        alpha_chars = [c for c in word if c.isalpha()]
        
        if not alpha_chars:
            return word
        
        # Reverse alphabetic characters
        reversed_alpha = alpha_chars[::-1]
        
        # Restore case of the original word
        if word.istitle():
            reversed_alpha[0] = reversed_alpha[0].upper()
            reversed_alpha[1:] = [c.lower() for c in reversed_alpha[1:]]
        elif word.isupper():
            reversed_alpha = [c.upper() for c in reversed_alpha]
        elif word.islower():
            reversed_alpha = [c.lower() for c in reversed_alpha]
        
        # Reconstruct the word, preserving non-alphabetic characters
        result = []
        alpha_index = 0
        for char in word:
            if char.isalpha():
                result.append(reversed_alpha[alpha_index])
                alpha_index += 1
            else:
                result.append(char)
        
        return ''.join(result)
    
    # Use regex to split the string while preserving punctuation and spaces
    tokens = re.findall(r'\b\w+\b|[^\w\s]+|\s+', input_string)
    
    # Process each token
    processed_tokens = [
        reverse_word(token) if re.match(r'\b\w+\b', token) else token 
        for token in tokens
    ]
    
    return ''.join(processed_tokens)