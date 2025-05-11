def get_num_words(text): # obtains word count
    words = text.split()
    return len(words)

def get_num_characters(text): # obtains unique character count after converting to lowercase
    char_count = {}
    text = text.lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count