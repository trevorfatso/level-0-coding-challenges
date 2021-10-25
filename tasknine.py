#task9
def vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = string.lower()
    string = list(string)
    vwls_string = []
    for i in string:
        if i in vowels:
            if i not in vwls_string:
                vwls_string.append(i)
    vwls_string = ', '.join(vwls_string)    
    print(f'Vowels: {vwls_string}')