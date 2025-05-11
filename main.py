def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
# handles text inputs
from stats import get_num_words
from stats import get_num_characters

def main(): # prints word count and character count
    book_text = get_book_text("books/frankenstein.txt")
    char_count = get_num_characters(book_text)
    
    print(f'{get_num_words(book_text)} words found in the document')   
    print(char_count)  

main()
