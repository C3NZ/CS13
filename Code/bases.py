#!python

import string

# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

# Create our char mappings for working with up to 36 bases
all_chars = string.digits + string.ascii_lowercase
chars = dict(zip(all_chars, range(len(all_chars))))


def decode(digits: str, base: int, is_fraction: bool = False) -> int or float:
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: float or int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, "base is out of range: {}".format(base)
    output_num = 0
    decimal_value = 0
    copied_digits = digits

    # check to see if the
    if "." in digits:
        broken_up = digits.split(".")
        digits = broken_up[0]
        decimal_value = decode(broken_up[1], base, is_fraction=True)

    # if the current number is a decimal, step and power need to be -1
    # and the digits can stay where they are. If it's not a decimal, step
    # needs to be 1 and power needs to be 0 with the digits reversed so we can
    # start with the least magnitude
    if is_fraction:
        step = -1
        power = -1
    else:
        copied_digits = digits[::-1]
        step = 1
        power = 0

    # Iterate through all the digits within the string backwards
    for curr_digit in copied_digits:
        output_num += chars[curr_digit.lower()] * (base ** power)
        power += step

    return output_num + decimal_value


def encode(number: int, base: int, is_fraction: bool = False) -> str:
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, "base is out of range: {}".format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, "number is negative: {}".format(number)
    output_list = []
    copy_num = number

    # Keep dividing the number as long as it's greater than 0
    while copy_num != 0:
        copy_num, remainder = divmod(copy_num, base)
        # Map the remainder to it's encoded representation
        output_list.append(all_chars[remainder])

    return "".join(output_list[::-1])


def convert(digits: str, base1: int, base2: int) -> str:
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, "base1 is out of range: {}".format(base1)
    assert 2 <= base2 <= 36, "base2 is out of range: {}".format(base2)

    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys

    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print("{} in base {} is {} in base {}".format(digits, base1, result, base2))
    else:
        print("Usage: {} digits base1 base2".format(sys.argv[0]))
        print("Converts digits from base1 to base2")


if __name__ == "__main__":
    main()
