#!/usr/bin/python3
"""
UTF-8 Validation:

Implement a function that checks if a given data set
is a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Returns: True if the data set is a valid UTF-8 encoding, otherwise
returns False.
A character in UTF-8 can be 1 to 4 bytes long.
The data set can contain multiple characters.
The data is represented by a list of integers.
Each integer represents 1 byte of data, so you only
need to consider the 8 least significant bits of each
integer.
"""

def validUTF8(data):
    """Validate UTF-8 encoding in a data set

    Args:
        data (list[int]): List of integers representing bytes.
    """
    remaining_bytes = 0

    bit_mask_1 = 1 << 7
    bit_mask_2 = 1 << 6

    for byte in data:

        leading_bit_mask = 1 << 7

        if remaining_bytes == 0:

            while leading_bit_mask & byte:
                remaining_bytes += 1
                leading_bit_mask = leading_bit_mask >> 1

            if remaining_bytes == 0:
                continue

            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

        else:
            if not (byte & bit_mask_1 and not (byte & bit_mask_2)):
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0
