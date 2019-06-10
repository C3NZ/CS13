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
    result_num = 0
    decimal_value = 0
    copied_digits = digits

    # check to see if the digits contains decimal point values
    if "." in digits:
        broken_up_digits = copied_digits.split(".")
        copied_digits = broken_up_digits[0]
        decimal_digits = broken_up_digits[1]
        decimal_value = decode(decimal_digits, base, is_fraction=True)

    # if the current number is a decimal, step and power need to be -1
    # and the digits can stay where they are. If it's not a decimal, step
    # needs to be 1 and power needs to be 0 with the digits reversed so we can
    # start with the least magnitude
    if is_fraction:
        step = -1
        power = -1
    else:
        copied_digits = copied_digits[::-1]
        step = 1
        power = 0

    # Iterate through all the digits (either reversed, or normal for fractional values)
    for curr_digit in copied_digits:
        lowercased_digit = curr_digit.lower()
        result_num += chars[lowercased_digit] * (base ** power)
        power += step

    return result_num + decimal_value


def encode(number: int, base: int) -> str:
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, "base is out of range: {}".format(number)
    # Handle unsigned numbers only for now
    assert number >= 0, "number is negative: {}".format(number)

    result_list = []
    whole_num = number

    whole_num = int(number // 1)
    decimal_value = number - whole_num

    # Keep dividing the number as long as it's greater than 0
    while whole_num != 0:
        whole_num, remainder = divmod(whole_num, base)
        print(remainder)
        # Map the remainder to it's encoded representation
        result_list.append(all_chars[remainder])

    # Check if there is a decimal value, if so reverse the list now
    # otherwise, return the current list
    if decimal_value:
        result_list = result_list[::-1]
        result_list.append(".")
    else:
        return "".join(reversed(result_list))

    # Encode the decimal point to it's respective base
    while decimal_value != 0:
        decimal_value = decimal_value * base
        # Obtain the whole number from our floating point valeu
        whole_num = int(decimal_value // 1)
        # Obtain just the decimal
        decimal_value = decimal_value - whole_num
        # Add our whole number mapping to the list
        result_list.append(all_chars[whole_num])

    return "".join(result_list)


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


def convert_negative_binary_nums(digits: str, base: int) -> str:
    """
        Convert negative binary numbers to a specific base 

        Args:
            digits - The binary digits we'd like to convert
            base - The base we'd like to convert to

        Return:
            A string containing the negative binary digits encoded to
            a new  base
    """
    bits = []
    is_negative = False

    # Check if the number is negative according to twos complement
    if digits[0] == "1":
        is_negative = True
        flip = False

        # Flip necessary bits
        for char in reversed(digits):

            if flip:
                bits.append("0" if char == "1" else "1")
            else:
                bits.append(char)

            if char == "1":
                flip = True

        bits = bits[::-1]

    resulting_value = encode(decode(bits or digits, 2), base)

    if is_negative:
        return "-" + resulting_value

    return resulting_value


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
