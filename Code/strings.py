#!python


def contains(text, pattern):
    """
        Return a boolean indicating whether pattern occurs in text.
        Runtime -> O(n * (m + i)) where:
            n is the length of the text to be checked
            m is the pattern to be compared to the substring
            i is the amount of times we need to compare the substring to the pattern 
    """
    assert isinstance(text, str), "text is not a string: {}".format(text)
    assert isinstance(pattern, str), "pattern is not a string: {}".format(text)
    text_len = len(text)

    # Check some conditions for matching basic patterns
    if len(text) == 0 and len(pattern) == 0:
        return True
    elif len(text) == 0:
        return False
    if len(pattern) == 0:
        return True

    for i in range(len(text)):
        print(i)
        if pattern[0] == text[i]:
            window = len(pattern) + i

            if window > text_len:
                return False

            if pattern == text[i:window]:
                return True
    return False


def find_index(text, pattern, starting_point=0):
    """
        Return the starting index of the first occurrence of pattern in text,
        or None if not found. 
        Runtime -> O(n + (m * i)) where: 
            n is the length of the text to be checked
            m is the pattern to be compared to the substring
    """
    assert isinstance(text, str), "text is not a string: {}".format(text)
    assert isinstance(pattern, str), "pattern is not a string: {}".format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    index = None
    text_len = len(text)

    if len(text) == 0 and len(pattern) == 0:
        return 0
    elif len(text) == 0:
        return index
    elif len(pattern) == 0:
        return starting_point

    for i in range(starting_point, len(text)):
        if pattern[0] == text[i]:
            window = len(pattern) + i

            if window > text_len:
                return None

            if pattern == text[i:window]:
                index = i
                return index

    return None


def find_all_indexes(text, pattern):
    """
        Return a list of starting indexes of all occurrences of pattern in text,
        or an empty list if not found. -> O(n * m) where n is the length of the text
        Runtime -> O(n + (m * i)) where:
            n is the length of the text to be checked
            m is the pattern to be compared to the substring
            i is the amount of times we need to compare the pattern to the substring
    """
    assert isinstance(text, str), "text is not a string: {}".format(text)
    assert isinstance(pattern, str), "pattern is not a string: {}".format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    indexes = []
    if len(text) == 0 and len(pattern) == 0:
        return 0
    elif len(text) == 0:
        return indexes

    starting_point = 0
    text_len = len(text)
    while starting_point != text_len:
        index = find_index(text, pattern, starting_point)
        if index == None:
            return indexes
        else:
            indexes.append(index)
            starting_point = index + 1

    return indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print("contains({!r}, {!r}) => {}".format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print("find_index({!r}, {!r}) => {}".format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print("find_all_indexes({!r}, {!r}) => {}".format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys

    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print("Usage: {} text pattern".format(script))
        print("Searches for occurrences of pattern in text")
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == "__main__":
    main()
