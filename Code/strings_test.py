#!python

import unittest

from strings import contains, find_all_indexes, find_index


class StringsTest(unittest.TestCase):
    def test_contains_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert contains("abc", "") is True  # all strings contain empty string
        assert contains("abc", "a") is True  # single letters are easy
        assert contains("abc", "b") is True
        assert contains("abc", "c") is True
        assert contains("abc", "ab") is True  # multiple letters are harder
        assert contains("abc", "bc") is True
        assert contains("abc", "abc") is True  # all strings contain themselves
        assert contains("aaa", "a") is True  # multiple occurrences
        assert contains("aaa", "aa") is True  # overlapping pattern
        assert contains("dogdogdogcatdogdogdog", "cat") is True
        assert contains("dogcatdogcatdogdogdog", "dog") is True
        assert contains("dogcatdogcatdogdogfog", "fog") is True

    def test_contains_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert contains("abc", "z") is False  # remember to test other letters
        assert contains("abc", "ac") is False  # important to test close cases
        assert contains("abc", "az") is False  # first letter, but not last
        assert contains("abc", "abz") is False  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is False statements
        assert contains("dogdogdogdogdogdog", "dogg") is False
        assert contains("dogdogdogdogdogdogdeeeeez", "deez") is False
        assert contains("hellodarknessmyoldfriend", "dankness") is False

    def test_contains_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert contains("ababc", "ab") is True  # multiple occurrences
        assert contains("banana", "na") is True  # multiple occurrences
        assert contains("ababc", "abc") is True  # overlapping prefix
        assert contains("bananas", "nas") is True  # overlapping prefix
        assert contains("BOOMBOOMBOMBBOOMB", "bomb") is True
        assert contains("havannaoonana", "nna") is True
        assert contains("**__yeet__**", "yeet") is True

    def test_find_index_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_index("abc", "") == 0  # all strings contain empty string
        assert find_index("abc", "a") == 0  # single letters are easy
        assert find_index("abc", "b") == 1
        assert find_index("abc", "c") == 2
        assert find_index("abc", "ab") == 0  # multiple letters are harder
        assert find_index("abc", "bc") == 1
        assert find_index("abc", "abc") == 0  # all strings contain themselves
        assert find_index("aaa", "a") == 0  # multiple occurrences
        assert find_index("aaa", "aa") == 0  # overlapping pattern
        assert find_index("yaaaaaaaaaYEETyaaaaaYEET", "yeet") == 10
        assert find_index("whome?aw hell nahhhhh", "aw") == 6
        assert find_index("I cant believe its not PYTHON", "python") == 23

    def test_find_index_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_index("abc", "z") is None  # remember to test other letters
        assert find_index("abc", "ac") is None  # important to test close cases
        assert find_index("abc", "az") is None  # first letter, but not last
        assert find_index("abc", "abz") is None  # first 2 letters, but not last
        assert find_index("yaaaaaayeeeeetyaaaaYEEET", "yeet") is None
        assert find_index("WHO Peed oN THE floor BROOM?", "peeed") is None
        assert find_index("YEAAAAAH IM GONNA TAKE MY HORSE...", "I'm") is None

    def test_find_index_with_complex_patterns(
        self
    ):  # Difficult test cases (examples) with complex patterns
        assert find_index("ababc", "abc") == 2  # overlapping prefix
        assert find_index("bananas", "nas") == 4  # overlapping prefix
        assert find_index("abcabcabc", "abc") == 0  # multiple occurrences
        assert find_index("abcabcab", "abc") == 0  # multiple occurrences
        assert find_index("abcabcdef", "abcd") == 3  # overlapping prefix
        assert find_index("abcabcdef", "abcdef") == 3  # overlapping prefix
        assert find_index("abcabcdabcde", "abcde") == 7  # overlapping prefix
        assert (
            find_index("abcabcdabcde", "abcd") == 3
        )  # multiple occurrences, overlapping prefix
        assert find_index("abra cadabra", "abra") == 0  # multiple occurrences
        assert find_index("abra cadabra", "adab") == 6  # overlapping prefix
        assert find_index("robots die on roblox", "rob") == 0
        assert find_index("roxbots die on roblox", "rob") == 15
        assert find_index("bro plz lemme hit your juul, just two hits", "juu") == 23
        assert (
            find_index("I got the horses in the back, horse stock is attached", "horse")
            == 10
        )

    def test_find_all_indexes_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_all_indexes("abc", "") == [
            0,
            1,
            2,
        ]  # all strings contain empty string
        assert find_all_indexes("abc", "a") == [0]  # single letters are easy
        assert find_all_indexes("abc", "b") == [1]
        assert find_all_indexes("abc", "c") == [2]
        assert find_all_indexes("abc", "ab") == [0]  # multiple letters are harder
        assert find_all_indexes("abc", "bc") == [1]
        assert find_all_indexes("abc", "abc") == [0]  # all strings contain themselves
        assert find_all_indexes("aaa", "a") == [0, 1, 2]  # multiple occurrences
        assert find_all_indexes("aaa", "aa") == [0, 1]  # overlapping pattern
        assert find_all_indexes(
            "I got the horses in the back, horse stock is attached", "horse"
        ) == [10, 30]
        assert find_all_indexes("bro plz lemme hit your juul, just two hits", "ju") == [
            23,
            29,
        ]
        assert find_all_indexes("robots die on roblox and robloxians win", "rob") == [
            0,
            14,
            25,
        ]

    def test_find_all_indexes_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_all_indexes("abc", "z") == []  # remember to test other letters
        assert find_all_indexes("abc", "ac") == []  # important to test close cases
        assert find_all_indexes("abc", "az") == []  # first letter, but not last
        assert find_all_indexes("abc", "abz") == []  # first 2 letters, but not last
        assert find_all_indexes("robots are invading robotland!", "roblox") == []
        assert (
            find_all_indexes(
                "I got the horxes in the back, horx stock is attached", "horse"
            )
            == []
        )
        assert find_all_indexes("yayeetyayeetyayeetyaaaa", "yeeet") == []

    def test_find_all_indexes_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_all_indexes("ababc", "abc") == [2]  # overlapping prefix
        assert find_all_indexes("bananas", "nas") == [4]  # overlapping prefix
        assert find_all_indexes("abcabcabc", "abc") == [0, 3, 6]  # multiple occurrences
        assert find_all_indexes("abcabcab", "abc") == [0, 3]  # multiple occurrences
        assert find_all_indexes("abcabcdef", "abcd") == [3]  # overlapping prefix
        assert find_all_indexes("abcabcdef", "abcdef") == [3]  # overlapping prefix
        assert find_all_indexes("abcabcdabcde", "abcde") == [7]  # overlapping prefix
        assert find_all_indexes("abcabcdabcde", "abcd") == [
            3,
            7,
        ]  # multiple occurrences, overlapping prefix
        assert find_all_indexes("abra cadabra", "abra") == [
            0,
            8,
        ]  # multiple occurrences
        assert find_all_indexes("abra cadabra", "adab") == [6]  # overlapping prefix
        assert find_all_indexes("yeetyeeeetyeetyeeetyeet", "yeet") == [0, 10, 19]
        assert find_all_indexes("hmmm, is there a pattern here?", "er") == [11, 21, 26]


if __name__ == "__main__":
    unittest.main()
