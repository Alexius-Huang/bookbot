def get_words_count(content):
    return len(content.split())

def get_char_counts(content):
    content = content.lower()
    result = {}

    for char in content:
        if not char in result:
            result[char] = 1
        else:
            result[char] += 1
    return result

def get_sorted_char_counts(content):
    char_counts = get_char_counts(content)
    char_nums = []

    for char in char_counts:
        if not char.isalpha():
            continue
        char_nums.append({ "char": char, "num": char_counts[char] })

    def sort_on(dict):
        return dict["num"]

    char_nums.sort(reverse=True, key=sort_on)
    return char_nums
