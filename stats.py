def word_counter(book):
    book_list = book.split()
    return len(book_list)


def char_counter(book):
    chars = {}
    for c in book:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars
    
def sort_on(items):
    return items["num"]

