import re

# match

txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I)

print(match)
span = match.span()
print(span)

start, end = span
print(start, end)
substring = txt[start: end]
print(substring)

txt = 'actually i like to teach python'
match = re.match('i like to teach', txt, re.I)
print(match)

txt = '''Python is the most beautiful language that a human being has ever created.
I recomend python for a first programming language'''

match = re.search('first', txt, re.I)
print(match)

span = match.span()
print(span)

start, end = span
print(start, end)

substring = txt[start: end]
print(substring)

# findall

matches = re.findall('python', txt, re.I)
print(matches)

matches = re.findall('python|Python', txt)
print(matches)

matches = re.findall('[Pp]ython', txt)
print(matches)

# replacing

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)

# or

match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)

scripted_txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

decripted_txt = re.sub('%', '', scripted_txt)
print(decripted_txt)


print(re.split('\n', decripted_txt))

# writing regex patterns

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '

matches = re.findall(regex_pattern, txt)
print(matches)

matches = re.findall(regex_pattern, txt, re.I)
print(matches)

regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)


    # []: A set of characters
    #     [a-c] means, a or b or c
    #     [a-z] means, any letter from a to z
    #     [A-Z] means, any character from A to Z
    #     [0-3] means, 0 or 1 or 2 or 3
    #     [0-9] means any number from 0 to 9
    #     [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
    # \: uses to escape special characters
    #     \d means: match where the string contains digits (numbers from 0-9)
    #     \D means: match where the string does not contain digits
    # . : any character except new line character(\n)
    # ^: starts with
    #     r'^substring' eg r'^love', a sentence that starts with a word love
    #     r'[^abc] means not a, not b, not c.
    # $: ends with
    #     r'substring$' eg r'love$', sentence that ends with a word love
    # *: zero or more times
    #     r'[a]*' means a optional or it can occur many times.
    # +: one or more times
    #     r'[a]+' means at least once (or more)
    # ?: zero or one time
    #     r'[a]?' means zero times or once
    # {3}: Exactly 3 characters
    # {3,}: At least 3 characters
    # {3,8}: 3 to 8 characters
    # |: Either or
    #     r'apple|banana' means either apple or a banana
    # (): Capture and group

regex_pattern = r'[Aa]pple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'[Aa]pple|[Bb]anana'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'\d+'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'[a].'
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'[a].+'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'[a].*'
matches = re.findall(regex_pattern, txt)
print(matches)

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''

regex_pattern = r'[Ee]-?mail'
matches = re.findall(regex_pattern, txt)
print(matches)

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'^This'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'[^A-Za-z ]+'
matches = re.findall(regex_pattern, txt)
print(matches)



