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

def sort_on(dict): 
    return dict["num"] 
# This is a gap in my learning path, see: "Python functions as first-class objects" or "higher-order functions in Python"

def get_sorted_list(char_dict):
    result_list = []
    for char, count in char_dict.items(): # tuple unpacking, adding each to a new char list
        new_char_dict = {"char": char, "num": count}
        result_list.append(new_char_dict)
    result_list.sort(reverse=True, key=sort_on)
    return result_list