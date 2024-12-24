def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        count = word_count(file_contents)
        character_count = count_characters(file_contents)
        char_list = []
        for key, value in character_count.items():
            if key.isalpha():
                char_list.append({key: value})
            char_list.sort(reverse=True, key=lambda d: list(d.values())[0])

        print(f"--- Begin report of {book_path} ---\n")
        print(f"Total number of words: {count}\n")
        for char_dict in char_list:
            char = list(char_dict.keys())[0]
            char_count = char_dict[char]
            print(f"The '{char}' character was found {char_count} times.")

    
def word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(text):
    lowered_text = text.lower()
    character_count = {}
    for character in lowered_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count

main()