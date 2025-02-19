import pytest
from string_converter import to_snake_case

def test_basic_camel_case():
    assert to_snake_case("helloWorld") == "hello_world"

def test_pascal_case():
    assert to_snake_case("HelloWorld") == "hello_world"

def test_existing_snake_case():
    assert to_snake_case("hello_world") == "hello_world"

def test_mixed_separators():
    assert to_snake_case("Hello-World Test") == "hello_world_test"

def test_special_characters():
    assert to_snake_case("Hello@World!123") == "hello_world_123"

def test_empty_string():
    assert to_snake_case("") == ""

def test_all_uppercase():
    assert to_snake_case("HELLO_WORLD") == "hello_world"

def test_error_non_string():
    with pytest.raises(TypeError):
        to_snake_case(123)
    with pytest.raises(TypeError):
        to_snake_case(None)