#!python


def search_string(text: str, pattern: str, starting_point: int = 0) -> int:
    """
        Search a text for a pattern given a starting point

        Arguments:
            text - The text we're searching through
            pattern - The pattern we're searching for
            starting_point - The point in the string we'd like to start at

        Return:
            int indicating if there was a match.
            We return i for the index that matched, or -1 for indicating
            that there was no match
    """
    text_len = len(text)
    for i in range(starting_point, len(text)):
        if pattern[0].lower() == text[i].lower():
            window = len(pattern) + i

            if window > text_len:
                return -1

            if pattern.lower() == text[i:window].lower():
                return i
    return -1


def check_strings(text: str, pattern: str) -> int:
    """
        Helper function for checking conditions on both the text and pattern
        to see if searching is needed at all.

        Arguments:
            text - The text we're searching through
            pattern - The pattern we're searching for

        Return:
            int that indicates a status.
            0  - Text is empty and so is the pattern, one match
            -1 - Text is empty but there is a pattern, no match
            1  - pattern is empty, meaning that there is a match
            2  - Text and pattern are both strings >= 1 character
    """
    if not text and not pattern:
        return 0
    elif not text:
        return -1
    elif not pattern:
        return 1
    else:
        return 2


def contains(text, pattern):
    """
        Return a boolean indicating whether pattern occurs in text.
        Runtime -> O(n + (m * i)) where:
            n - is the length of the text to be checked
            m - is the pattern to be compared to the substring
            i - is the amount of times we need to compare the
                substring to the pattern
    """
    assert isinstance(text, str), "text is not a string: {}".format(text)
    assert isinstance(pattern, str), "pattern is not a string: {}".format(text)

    checked = check_strings(text, pattern)

    if checked in (0, 1):
        return True

    if checked == -1:
        return False

    result = search_string(text, pattern)

    return True if result >= 0 else False


def find_index(text, pattern, starting_point=0):
    """
        Return the starting index of the first occurrence of pattern in text,
        or None if not found. 
        Runtime -> O(n + (m * i)) where: 
            n - is the length of the text to be checked
            m - is the pattern to be compared to the substring
            i - is the amount of times we need to compare the pattern to the 
                substring
    """
    assert isinstance(text, str), "text is not a string: {}".format(text)
    assert isinstance(pattern, str), "pattern is not a string: {}".format(text)

    checked = check_strings(text, pattern)

    if checked in (0, 1):
        return starting_point

    if checked == -1:
        return None

    result = search_string(text, pattern, starting_point)
    return result if result >= 0 else None


def find_all_indexes(text, pattern):
    """
        Return a list of starting indexes of all occurrences of 
        pattern in text, or an empty list if not found.
        Runtime -> O(n + (m * i)) where:
            n is the length of the text to be checked
            m is the pattern to be compared to the substring
            i is the amount of times we need to compare the pattern to the substring
    """
    assert isinstance(text, str), "text is not a string: {}".format(text)
    assert isinstance(pattern, str), "pattern is not a string: {}".format(text)

    checked = check_strings(text, pattern)

    print(checked)
    if checked == 0:
        return []
    elif checked == -1:
        return None

    # Setup our list of indexes, the starting point, and length of text
    indexes = []
    starting_point = 0
    text_len = len(text)

    # Iterate through the entire string
    while starting_point != text_len:
        index = find_index(text, pattern, starting_point)

        if index is None:
            return indexes

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
