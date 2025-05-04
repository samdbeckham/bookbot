def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    chars = {}
    for char in text:
        lchar = char.lower()
        if lchar in chars:
            chars[lchar] += 1
        else:
            chars[lchar] = 1
    return chars

def sort_chars(chars):
    sortable_list = []
    def sort_on(dict):
        return dict["num"]
    for char in chars:
        sortable_list.append({"char": char, "num": chars[char]})
    sortable_list.sort(reverse=True,key=sort_on)
    return sortable_list



