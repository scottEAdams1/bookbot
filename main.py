def main():
    name = "books/frankenstein.txt"
    text = get_text(name)
    length = get_word_count(text)
    char_count = get_char_count(text)
    char_list = dictionary_to_sorted_list(char_count)
    print(f"--- Begin report of {name} ---")
    print(f"{length} words found in the document\n")
    for character in char_list:
        if character["char"].isalpha():
            print(f"The '{character['char']}' character was found {character['num']} times")
    print("--- End report ---")

def get_text(name):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    words = text.split()
    length = len(words)
    return length

def get_char_count(text):
    lower_case_text = text.lower()
    char_count = {}
    words = lower_case_text.split()
    for word in words:
        for letter in word:
            if letter not in char_count:
                char_count[letter] = 1
            else:
                char_count[letter] = char_count[letter] + 1
    return char_count

def sort_on(dictionary):
    return dictionary["num"]

def dictionary_to_sorted_list(dictionary):
    char_list = []
    for character in dictionary:
        char_list.append({"char": character, "num": dictionary[character]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()