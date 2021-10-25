#task10 
def common_chars(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    string1 = list(string1)
    string2 = list(string2)
    common_char = []
    for i in string1:
        if i in string2:
            if i not in common_char:
                common_char.append(i)
    common_char = ', '.join(common_char)
    if common_char == '':
        print('There are no common characters between these words.')
    else:
        print(f'Common letters: {common_char}')