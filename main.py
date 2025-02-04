def main():
    file = "books/frankenstein.txt"
    file_content = read_file(file)
    word_count = count_words(file_content)
    letter_count = count_letters(file_content)
    report_data = listed_report(letter_count)
    print(file_content)
    print(word_count)
    print(letter_count)
    report_data.sort(reverse=True, key=sort_on)
    report_message(file, word_count, report_data)

def report_message(file, word_count, report_data):
    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words found in the document")
    print("")
    for i in range(len(report_data)):
        if report_data[i]["letter"].isalpha():
            print(f"The '{report_data[i]["letter"]}' character was found {report_data[i]["count"]} times")
    print("--- End report ---")


def listed_report(letters):
    new_dict = []
    for l, c in letters.items():
        list = {"letter": l, "count": c}
        new_dict.append(list)
    return new_dict

def sort_on(by):
    return by["count"]
    
def read_file(file):
    with open(file) as f:
        file_content = f.read()
        return file_content

def count_words(content):
    words = content.split()
    return len(words)

def count_letters(content):
    lowercase_letters = content.lower()
    count_chars = {}
    for letter in lowercase_letters:
        if letter in count_chars:
            count_chars[letter] += 1
        else:
            count_chars[letter] = 1
    return count_chars
        
main()