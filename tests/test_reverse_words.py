import pytest
from src.reverse_words import reverse_words_in_string

def test_reverse_words_basic():
    assert reverse_words_in_string("Hello World") == "olleH dlroW"

def test_reverse_words_with_punctuation():
    assert reverse_words_in_string("Hello, World!") == "olleH, dlroW!"

def test_reverse_words_mixed_case():
    assert reverse_words_in_string("Hello World") == "olleH dlroW"
    assert reverse_words_in_string("HELLO WORLD") == "OLLEH DLROW"
    assert reverse_words_in_string("hello world") == "olleh dlrow"

def test_reverse_words_multiple_spaces():
    assert reverse_words_in_string("  Hello   World  ") == "  olleH   dlroW  "

def test_reverse_words_with_numbers():
    assert reverse_words_in_string("Hello123 World456") == "olleH321 dlroW654"

def test_reverse_words_empty_string():
    assert reverse_words_in_string("") == ""

def test_reverse_words_single_word():
    assert reverse_words_in_string("Hello") == "olleH"

def test_reverse_words_complex_mixed_case():
    assert reverse_words_in_string("Hello, World! How Are You?") == "olleH, dlroW! woH erA ouY?"

def test_reverse_words_with_special_characters():
    assert reverse_words_in_string("Hello@World#123") == "olleH@dlroW#321"