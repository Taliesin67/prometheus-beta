import pytest
from src.even_number_remover import remove_and_sum_even_numbers

def test_remove_and_sum_even_numbers():
    # Test case 1: Mixed numbers
    numbers1 = [1, 2, 3, 4, 5, 6]
    result1 = remove_and_sum_even_numbers(numbers1)
    assert result1 == 12
    assert numbers1 == [1, 3, 5]

    # Test case 2: Only even numbers
    numbers2 = [2, 4, 6, 8]
    result2 = remove_and_sum_even_numbers(numbers2)
    assert result2 == 20
    assert numbers2 == []

    # Test case 3: Only odd numbers
    numbers3 = [1, 3, 5, 7]
    result3 = remove_and_sum_even_numbers(numbers3)
    assert result3 == 0
    assert numbers3 == [1, 3, 5, 7]

    # Test case 4: Empty list
    numbers4 = []
    result4 = remove_and_sum_even_numbers(numbers4)
    assert result4 == 0
    assert numbers4 == []

    # Test case 5: Negative numbers
    numbers5 = [-1, -2, -3, -4, 0]
    result5 = remove_and_sum_even_numbers(numbers5)
    assert result5 == -6
    assert numbers5 == [-1, -3]