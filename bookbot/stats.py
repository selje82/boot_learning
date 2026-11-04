def word_count(book_text: str) -> int:
    words = book_text.split()
    return len(words)

def symbol_count(book_text: str):
    symbol_dict = {}
    for symbol in book_text:
        if symbol in symbol_dict:
            symbol_dict[symbol] += 1
        else:
            symbol_dict[symbol] = 1
    return symbol_dict

def sort_on(book_count: tuple[str, int]) -> int:
    return book_count[1]

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    char_list = []
    for key, value in chars_dict.items():
        char_list.append((key, value))
    return sorted(char_list, key=sort_on, reverse=True)
