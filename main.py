
import sys 
from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath): # handles text inputs
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(): # prints word count and character count
    path = sys.argv[1] 
    book_text = get_book_text(path)
    word_count = get_num_words(book_text)
    char_count = get_num_characters(book_text)
    sorted_chars = get_sorted_list(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()
