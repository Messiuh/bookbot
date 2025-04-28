from stats import count_words, count_characters, sort_dict

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents 

def main():
    book_path ="books/frankenstein.txt"
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    char_dict = count_characters(book_text)
    report = sort_dict(char_dict)

    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in report:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

    
if __name__ == "__main__":
    main()

