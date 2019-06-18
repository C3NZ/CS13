"""
    Permutation and anagram generating functions
"""
import strings
from recursion import fast_permutation

STR_LIST = "abcdefghijklmnopqrstuvwxyz"


def generate_permutation(
    iterable: list = [], num_items: int = 3, use_letters: bool = False
):
    if not iterable:
        if use_letters:
            orig_list = [STR_LIST[i] for i in range(num_items)]
            all_perms = fast_permutation(orig_list, num_items)
        else:
            orig_list = [str(i) for i in range(num_items)]
            all_perms = fast_permutation(orig_list, num_items)

        return all_perms
    else:
        all_perms = fast_permutation(iterable, len(iterable))

        return all_perms


print(generate_permutation(num_items=5))
