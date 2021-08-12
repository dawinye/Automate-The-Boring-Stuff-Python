import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print("Group 1: " + mo.group(1))
print("Group 2: " + mo.group(2))
print("mo.group() " + mo.group())
print(mo.groups())


''' If you want to detect these characters as part of your text pattern, you
need to escape them with a backslash:
\. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \) '''


# | is or
# ()? is optional
# ()* is 0 or more
# ()+ is 1 or more
# (){specific number} matches repetitions
# greedy matching is default (Ha){3,5} will tr to match the longest one possible, so 5
# non-greedy matching is used with (Ha){3,5}? (question mark after the braces) and will try to match the shortest

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

#findall returns a list of strings with the matches, must have no gorups

''' \d Any numeric digit from 0 to 9.
\D Any character that is not a numeric digit from 0 to 9.
\w Any letter, numeric digit, or the underscore character.
(Think of this as matching “word” characters.)
\W Any character that is not a letter, numeric digit, or the
underscore character.
\s Any space, tab, or newline character. (Think of this as
matching “space” characters.)
\S Any character that is not a space, tab, or newline. '''


# [] creates custom character classes

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
##['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']


# ^ at the beginning of the string indicate that the regex must start with that, $ indicates it must end with the pattern
# ^something$ would indicate the regex must be made solely of that something

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
#['cat', 'hat', 'sat', 'lat', 'mat']

# (.*) matches anything

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
#'Al'
mo.group(2)
#'Sweigart'

# passing re.DOTALL as a second parameter to .compile() 
