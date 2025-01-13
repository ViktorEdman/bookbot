def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        for count in char_count:
            print(f"The '{count["char"]}' character was found {count["count"]} times")
        print("--- End report ---")


def count_words(str):
    words = str.split()
    return len(words)

def count_characters(str):
    char_dict = {}
    for char in str:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
            continue
        char_dict[char.lower()] = 0

    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({"char": char, "count": char_dict[char]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["count"]

main()
