spam = ['apples', 'bananas', 'tofu', 'cats']

def commacode(list):
    string = ''
    if len(list) == 0:
        return "this list is empty"
    for i in range(len(list)):
        if i != len(list)-1:
            string += list[i] + ", "
        else:
            string += "and " + list[i] + "."

    return string

print(commacode(spam))
