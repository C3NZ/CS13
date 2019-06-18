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
    input_word = "".join(char_list)
    anagrams = []

    # Iterate through all the permutations and see if any permutation
    # generated an anagram
    for perm in all_perms:
        if perm != input_word and perm in WORD_SET:
            anagrams.append(perm)

    return anagrams


print(generate_permutations(num_items=5))
print(generate_anagram(list("aeprs")))
