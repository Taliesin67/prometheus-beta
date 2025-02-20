def remove_and_sum_even_numbers(numbers):
    """
    Remove even numbers from the input array and return their sum.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: The sum of even numbers that were removed
    """
    # Separate even and odd numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    # Calculate sum of even numbers
    even_sum = sum(even_numbers)
    
    # Modify the original list to only contain odd numbers
    numbers.clear()
    numbers.extend(odd_numbers)
    
    return even_sum