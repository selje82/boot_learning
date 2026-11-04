import sys
from stats import word_count, symbol_count, sort_on, chars_dict_to_sorted_list

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def print_report(book_path: str, word_count: int, sorted_list: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for (char, count) in sorted_list:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) >= 2:
        content = get_book_text(sys.argv[1])
        print_report(sys.argv[1], word_count(content), chars_dict_to_sorted_list(symbol_count(content.lower())))
    else:
        sys.exit(1)


main()