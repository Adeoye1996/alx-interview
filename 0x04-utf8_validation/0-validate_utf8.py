#!/usr/bin/python3
"""
UTF-8 Validation:

Write a method that determines if a given data set
represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else
return False.
A character in UTF-8 can be 1 to 4 bytes long.
The data set can contain multiple characters.
The data will be represented by a list of integers.
Each integer represents 1 byte of data, therefore you
only need to handle the 8 least significant bits of each
integer.
"""


def validUTF8(data):
    """Determines if a data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers representing bytes.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7

        if num_bytes == 0:
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
