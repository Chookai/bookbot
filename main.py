
from stats import word_counter, char_counter, sort_on
import sys
def get_book_text(filepath):
    
    with open(filepath) as f:
        return f.read()

def print_report(num_words, converted):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in converted:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    relative_path = sys.argv[1]
    text = get_book_text(relative_path)
    num_words = word_counter(text)
    
    char_list = char_counter(text)
    converted = [{"char": char, "num": freq} for char, freq in char_list.items()]
    converted.sort(reverse=True, key=sort_on) 
    print_report(num_words, converted)

    
main()


