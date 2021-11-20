"""
File: anagram.py
Name: Rebecca
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
python_dict = {}  # all words in dictionary.txt


def main():
    """
    Finding all the anagram(s) for the word input by user.
    """
    ####################
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        start = time.time()
        all_word = []
        if word == EXIT:
            break
        find_anagrams(word, all_word)
        print('Searching...')
        print(f'{len(all_word)} anagrams: {all_word}')
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    Reading out the file and saving as dict.
    """
    global python_dict
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            python_dict[line] = 0


def find_anagrams(s, all_word):
    """
    :param s: word user input
    :param all_word: all the anagram(s)
    """
    find_anagrams_helper(s, '', string_to_number(s), all_word)


def find_anagrams_helper(s, current_string, number, all_word):
    """
    :param s: word user input
    :param current_string: string of number which keep updating to find all anagram(s)
    :param number: string of int which transfer by the word
    :param all_word: all the anagram(s)
    """
    if has_prefix(s, current_string):
        if len(current_string) == len(s):
            word = number_to_string(s, current_string)
            if word in python_dict and word not in all_word:
                print('Searching...')
                print(f'Found: {word}')
                all_word.append(word)
        else:
            for ele in number:
                if ele in current_string:
                    pass
                else:
                    current_string += ele  # Choose
                    find_anagrams_helper(s, current_string, number, all_word)  # Explore
                    current_string = current_string[:-1]  # Un-choose


def has_prefix(s, sub_s):
    """
    :param s: word user input
    :param sub_s: current string of int
    :return: True or False
    """
    ch = ''
    for i in sub_s:
        ch += s[int(i)]
    for ele in python_dict:
        if ele.startswith(ch):
            return True
    return False


def string_to_number(s):
    """
    :param s: word user input
    :return number: transfer the word into int
    """
    number = ''
    n = 0
    number += str(n)
    for i in range(len(s)-1):
        n += 1
        number += str(n)
    return number


def number_to_string(s, number):
    """
    :param s: word user input
    :param number: string of int which represent possible anagram
    :return: word of alphabet
    """
    word = ''
    for i in number:
        word += s[int(i)]
    return word


if __name__ == '__main__':
    main()
