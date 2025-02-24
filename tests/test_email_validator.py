import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test various valid email formats."""
    valid_emails = [
        'user@example.com',
        'user.name@example.com',
        'user+tag@example.com',
        'user-name@example.co.uk',
        'user123@example.org',
        'user.name123@example-domain.com'
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats."""
    invalid_emails = [
        '',  # Empty string
        'invalid-email',  # No @ symbol
        'user@',  # No domain
        '@example.com',  # No local part
        'user@.com',  # Invalid domain
        'user@example',  # No top-level domain
        'user@example..com',  # Double dot in domain
        'user@example.c',  # Too short top-level domain
        'user name@example.com',  # Space in local part
        'user@example.com ',  # Trailing space
        ' user@example.com',  # Leading space
        None,  # None input
        123,  # Non-string input
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_email_length_limits():
    """Test email length constraints."""
    # Local part max 64 characters
    long_local = 'a' * 65 + '@example.com'
    assert validate_email(long_local) is False

    # Total email max 254 characters
    long_email = 'a' * 200 + '@' + 'b' * 50 + '.com'
    assert validate_email(long_email) is False

def test_special_characters():
    """Test emails with special characters."""
    special_valid_emails = [
        'user.name@example.com',
        'user+tag@example.com',
        'user-name@example.co.uk',
    ]
    for email in special_valid_emails:
        assert validate_email(email) is True

def test_international_domains():
    """Test emails with international domain names."""
    international_valid_emails = [
        'user@example.co.uk',
        'user@subdomain.example.com',
        'user@example-domain.com'
    ]
    for email in international_valid_emails:
        assert validate_email(email) is True