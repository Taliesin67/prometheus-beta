import pytest
from src.alternating_case import convert_to_alternating_case

def test_convert_to_alternating_case_basic():
    """Test basic alternating case conversion."""
    assert convert_to_alternating_case("hello") == "HeLlO"

def test_convert_to_alternating_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_case("") == ""

def test_convert_to_alternating_case_with_spaces():
    """Test conversion of a string with spaces."""
    assert convert_to_alternating_case("hello world") == "HeLlO WoRlD"

def test_convert_to_alternating_case_mixed_case():
    """Test conversion of a string with mixed case."""
    assert convert_to_alternating_case("MiXeD CaSe") == "MiXeD CaSe"

def test_convert_to_alternating_case_non_alphabetic():
    """Test conversion of a string with non-alphabetic characters."""
    assert convert_to_alternating_case("hello123!@#") == "HeLlO123!@#"

def test_convert_to_alternating_case_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_case(None)