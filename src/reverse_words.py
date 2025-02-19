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
    
    # Split the string into words, preserving punctuation
    word_pattern = re.compile(r'(\w+|[^\w\s])')
    tokens = word_pattern.findall(input_string)
    
    # Process tokens to reverse words while maintaining capitalization
    processed_tokens = []
    current_word = []
    
    for token in tokens:
        # If token is punctuation or non-word, add to processed tokens
        if not token.isalnum():
            processed_tokens.append(token)
            continue
        
        # If it's a word, collect characters
        current_word.append(token)
    
    # Reverse each word while preserving original capitalization
    reversed_words = []
    for word in current_word:
        # Determine original capitalization
        if word.istitle():
            # If original word was title case, capitalize first letter of reversed word
            reversed_word = word[::-1].capitalize()
        elif word.isupper():
            # If original word was all uppercase, keep it uppercase
            reversed_word = word[::-1].upper()
        elif word.islower():
            # If original word was lowercase, keep it lowercase
            reversed_word = word[::-1].lower()
        else:
            # Mixed case, just reverse as-is
            reversed_word = word[::-1]
        
        reversed_words.append(reversed_word)
    
    # Combine processed tokens with reversed words
    result_tokens = []
    word_index = 0
    for token in tokens:
        if token.isalnum():
            result_tokens.append(reversed_words[word_index])
            word_index += 1
        else:
            result_tokens.append(token)
    
    return ''.join(result_tokens)