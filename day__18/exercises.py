import re

# 1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
letters = re.sub('[,.]', '', paragraph).split(' ')
quantify_list = set()

for letter in letters:
    quantify_list.add((len(re.findall(letter, paragraph)), letter))
quantify_list = list(quantify_list)
quantify_list.sort(reverse=True)
# print(quantify_list)

# 2
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
regex = r'[-]?\d+'
points = re.findall(regex, txt)
sorted_points = list(map(int, points))
distance = sorted_points[-1] - sorted_points[0]
# print(distance)

# 3

def is_valid_variable(arg):
    regex = r'^\d|[-]'
    matches = re.findall(regex, arg)
    return len(matches) == 0

# print(is_valid_variable('firstname'))

# 4
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(arg):
    regex = r'[@%$&;#!?]'
    return re.sub(regex, '', arg)

def quantify_paragraph(word, paragraph):
    regex = rf'([^\w]{word}[^\w])|(^{word}[^\w])|([^\w]{word}$)'
    results = re.findall(regex, paragraph)
    return (len(results), word)

def most_frequent_words(arg):
    words = re.sub('[.,]', '', arg).split(' ')
    quantified = set()
    for word in words:
        quantified.add(quantify_paragraph(word, arg))
    most_frequent = list(quantified)
    most_frequent.sort(reverse=True)
    return [i for index, i in enumerate(most_frequent) if index < 3]
print(most_frequent_words(clean_text(sentence)))
