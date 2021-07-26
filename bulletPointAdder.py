#! python3
# bulletPointAdder.py takes the clipboard and modifies it to have a star and space, then puts it back onto the clipboard

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)): #loop through all the indexes in the list
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
