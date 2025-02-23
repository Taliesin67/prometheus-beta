import pytest
from src.array_sum import calculate_array_sum

def test_calculate_array_sum_positive_integers():
    """Test sum of positive integers"""
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_calculate_array_sum_negative_integers():
    """Test sum of negative integers"""
    assert calculate_array_sum([-1, -2, -3]) == -6

def test_calculate_array_sum_mixed_numbers():
    """Test sum of mixed positive and negative numbers"""
    assert calculate_array_sum([-1, 0, 1, 2.5]) == 2.5

def test_calculate_array_sum_empty_list():
    """Test sum of an empty list"""
    assert calculate_array_sum([]) == 0

def test_calculate_array_sum_single_element():
    """Test sum of a single element list"""
    assert calculate_array_sum([42]) == 42

def test_calculate_array_sum_invalid_input_type():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_calculate_array_sum_non_numeric_elements():
    """Test error handling for non-numeric list elements"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "three"])