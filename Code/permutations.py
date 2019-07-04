"""
    Permutation and anagram generating functions
"""
import strings
from recursion import fast_permutation

STR_LIST = "abcdefghijklmnopqrstuvwxyz"


def create_word_set() -> set:
    """
        Generate a set of words from a unix based word file
    """
    word_list = []
    with open("/usr/share/dict/words", "r") as word_file:
        for line in word_file:
            word_list.append(line.strip())

    return set(word_list)


WORD_SET = create_word_set()


def generate_permutations(
    char_list: list = [], num_items: int = 3, use_letters: bool = False
) -> list:
    """
        Generate permutations based on the input specified by the user

        Arguments:
            char_list - The list of characters to permutate
            num_items - If char_list isn't specified, will be used for
                        generating a list of num_items chars
            use_letters - specifies if we should use characters for
                          generating characters

        Returns:
            A list of all permutations our algorithm generated
    """
    if not char_list:
        if use_letters:
            orig_list = [STR_LIST[i] for i in range(num_items)]
            all_perms = fast_permutation(orig_list, num_items)
        else:
            orig_list = [str(i) for i in range(num_items)]
            all_perms = fast_permutation(orig_list, num_items)

        return all_perms
    else:
        all_perms = fast_permutation(char_list, len(char_list))

        return all_perms


def generate_anagram(char_list: list = []):
    """
        Generate algorithms based on our permutation generating function

        Arguments:
            char_list - The list of letters we're trying to generate anagrams of
        Returns:
            A list of all the anagrams that can be made given an input
    """
    all_perms = generate_permutations(char_list)
    anagrams = []

    # Iterate through all the permutations and see if any permutation
    # generated an anagram
    for perm in all_perms:
        if perm in WORD_SET and perm not in anagrams:
            anagrams.append(perm)

    return anagrams


def word_jumble():
    word_list = ["tefon", "sokik", "niumem", "siconu"]
    wanted_chars = [(2, 4), (0, 1, 3), (4,), (3, 4)]
    unscrambled_words = []

    # iterate through every word in the word list and generate all anagrams
    for word in word_list:
        current_word = list(word)
        all_anagrams = generate_anagram(current_word)
        unscrambled_words.extend(all_anagrams)

    chars_at_position = []
    for i in range(len(unscrambled_words)):
        curr_list = []
        for position in wanted_chars[i]:
            curr_list.append(unscrambled_words[i][position])

        chars_at_position.extend(curr_list)
    print(unscrambled_words)
    print(chars_at_position)

    for i in range(len(chars_at_position)):
        for j in range(i + 1, len(chars_at_position)):
            curr_letters = [chars_at_position[i] + chars_at_position[j]]
            first_word = generate_anagram(curr_letters)

            if first_word:
                other_word = []
                for k in range(len(chars_at_position)):

                    if k != i and k != j:
                        other_word.append(chars_at_position[k])

                second_word = generate_anagram(other_word)

                if first_word and second_word:
                    print("".join(first_word) + "-" + "".join(second_word))


word_jumble()
