def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    char_dict = {}
    for char in file_contents:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict_item):
    return dict_item["num"]

def sort_dict(char_dict):
    report_list = []
    for char, count in char_dict.items():
        report_info = {"char": char, "num": count}
        report_list.append(report_info)

    report_list.sort(key=sort_on, reverse=True)
    return report_list


    
    




        
