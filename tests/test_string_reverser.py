import pytest
from src.string_reverser import reverse_string

def test_reverse_string_normal():
    """Test reversing a normal string"""
    assert reverse_string("hello") == "olleh"

def test_reverse_string_empty():
    """Test reversing an empty string"""
    assert reverse_string("") == ""

def test_reverse_string_single_char():
    """Test reversing a single character"""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    """Test reversing a string with spaces"""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    """Test reversing a string with special characters"""
    assert reverse_string("a1b2c3!@#") == "#@!3c2b1a"

def test_reverse_string_unicode():
    """Test reversing a string with unicode characters"""
    assert reverse_string("café") == "éfac"