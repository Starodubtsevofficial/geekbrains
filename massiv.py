def filter_strings(strings):
    new_strings = []
    for s in strings:
        if len(s) <= 3:
            new_strings.append(s)
    return new_strings

original_strings = input("Введите массив строк, разделенных запятой: ").split(',')

