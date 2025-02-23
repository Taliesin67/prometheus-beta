"""
Test suite for LZP Compression Algorithm
"""

import pytest
import random
from src.lzp_compression import LZPCompressor

def test_lzp_compressor_initialization():
    """Test initialization of LZPCompressor"""
    compressor = LZPCompressor()
    assert compressor.context_length == 8

def test_lzp_compression_empty_input():
    """Test compression of empty input"""
    compressor = LZPCompressor()
    assert compressor.compress(b'') == []
    assert compressor.compress('') == []

def test_lzp_decompression_empty_input():
    """Test decompression of empty input"""
    compressor = LZPCompressor()
    assert compressor.decompress([]) == b''

def test_lzp_compression_and_decompression_basic():
    """Test basic compression and decompression"""
    compressor = LZPCompressor()
    test_data = b'hello world'
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzp_compression_and_decompression_repeated_patterns():
    """Test compression and decompression with repeated patterns"""
    compressor = LZPCompressor()
    test_data = b'abcabcabcabc' * 10
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzp_compression_and_decompression_random_data():
    """Test compression and decompression with random data"""
    compressor = LZPCompressor()
    
    # Generate random bytes
    random.seed(42)  # Ensure reproducibility
    test_data = bytes(random.randint(0, 255) for _ in range(1000))
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzp_string_input():
    """Test compression and decompression with string input"""
    compressor = LZPCompressor()
    test_data = 'hello world'
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data.encode('utf-8')

def test_lzp_different_context_lengths():
    """Test compression with different context lengths"""
    for context_length in [4, 8, 16]:
        compressor = LZPCompressor(context_length)
        test_data = b'abcdefghijklmnopqrstuvwxyz' * 10
        
        # Compress
        compressed = compressor.compress(test_data)
        
        # Decompress
        decompressed = compressor.decompress(compressed)
        
        assert decompressed == test_data