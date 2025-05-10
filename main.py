def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def num_words(text):
    words = text.split()
    return len(words)

def main():
    print(f'{num_words(get_book_text("books/frankenstein.txt"))} words found in the document')
    
main()
