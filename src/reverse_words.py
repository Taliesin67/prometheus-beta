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
    
    def custom_case_reverse(word):
        """
        Reverse a word with custom case handling
        """
        # If no alphabetic characters, return as-is
        if not any(c.isalpha() for c in word):
            return word
        
        # Separate alphabetic and non-alphabetic parts
        chars = list(word)
        
        # Find alpha characters
        alpha_indices = [i for i, c in enumerate(chars) if c.isalpha()]
        
        # Reverse only alphabetic characters
        alpha_chars = [chars[i] for i in alpha_indices]
        alpha_chars_reversed = alpha_chars[::-1]
        
        # Restore original case pattern
        for i, idx in enumerate(alpha_indices):
            # Determine correct case based on original character
            if chars[idx].isupper():
                alpha_chars_reversed[i] = alpha_chars_reversed[i].upper()
            else:
                alpha_chars_reversed[i] = alpha_chars_reversed[i].lower()
        
        # Rebuild the word
        result = chars.copy()
        for i, (idx, char) in enumerate(zip(alpha_indices, alpha_chars_reversed)):
            result[idx] = char
        
        return ''.join(result)
    
    # Tokenize the string while preserving structure
    tokens = re.findall(r'\b\w+\b|[^\w\s]+|\s+', input_string)
    
    # Process words 
    processed_tokens = [
        custom_case_reverse(token) if re.match(r'\b\w+\b', token) else token 
        for token in tokens
    ]
    
    return ''.join(processed_tokens)