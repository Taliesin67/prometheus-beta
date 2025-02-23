"""
LZP (Lempel-Ziv Prediction) Compression Algorithm Implementation

This module provides functions for LZP compression and decompression.
LZP is a lossless compression algorithm that uses prediction based on 
previous context to improve compression efficiency.
"""

class LZPCompressor:
    def __init__(self, context_length=8):
        """
        Initialize the LZP compressor.
        
        :param context_length: Length of context used for prediction (default 8)
        """
        self.context_length = context_length
    
    def compress(self, data):
        """
        Compress the input data using LZP compression.
        
        :param data: Input data to compress (bytes or string)
        :return: Compressed data as a list of bytes
        """
        # Ensure input is bytes
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Validate input
        if not data:
            return []
        
        compressed = []
        context_buffer = bytearray(self.context_length)
        
        for byte in data:
            # Check if current context matches prediction
            predicted = self._predict_byte(context_buffer)
            
            if predicted == byte:
                # If predicted correctly, add a match flag
                compressed.append(1)
            else:
                # If prediction fails, add a literal flag and the actual byte
                compressed.append(0)
                compressed.append(byte)
            
            # Update context buffer
            context_buffer = context_buffer[1:] + bytearray([byte])
        
        return compressed
    
    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZP algorithm.
        
        :param compressed_data: Compressed data to decompress
        :return: Decompressed data as bytes
        """
        # Validate input
        if not compressed_data:
            return b''
        
        decompressed = bytearray()
        context_buffer = bytearray(self.context_length)
        
        i = 0
        while i < len(compressed_data):
            if compressed_data[i] == 1:
                # Predicted byte match
                predicted = self._predict_byte(context_buffer)
                byte = predicted
            else:
                # Literal byte
                i += 1
                if i >= len(compressed_data):
                    break
                byte = compressed_data[i]
            
            # Add byte to decompressed data
            decompressed.append(byte)
            
            # Update context buffer
            context_buffer = context_buffer[1:] + bytearray([byte])
            
            i += 1
        
        return bytes(decompressed)
    
    def _predict_byte(self, context_buffer):
        """
        Simple prediction method based on context.
        For this implementation, use a simple hash of the context.
        
        :param context_buffer: Current context buffer
        :return: Predicted byte
        """
        if len(context_buffer) < self.context_length:
            # If context is not full, return a default prediction
            return 0
        
        # Use a simple hash of the context as prediction
        prediction = sum(context_buffer) % 256
        return prediction