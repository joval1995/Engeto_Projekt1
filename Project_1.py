'''
author = JOZEFÍNA 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

separator = '-' * 40
reg_users = {'bob' : '123', 'ann' : 'pass123', 'mike' : 'password123', 'liz' : 'pass123'}
input_data = (input('Username: '), input('Password: '))


for user_data in reg_users.items():
    if input_data == user_data:
        print('Welcome to the app ' + input_data[0] + '.' + '\n' + 'We have 3 texts to be analyzed.')
        break
else:
    print('Sorry, the user is not registered. The program ends.')
    quit()


print(separator)
num_of_text = input('Enter a number btw 1 and 3 to select: ')


if num_of_text.isnumeric():
    num_of_text = int(num_of_text) - 1
    if 0 <= num_of_text < 3:
        one_text = TEXTS[num_of_text].split(' ')
    else:
        print('Sorry, text number ', num_of_text + 1,' does not exist. The program ends.')
        quit()
else:
    print('Sorry, ' + num_of_text + ' is not number. The program ends.')
    quit()


print(separator)


print_words = []
for word in one_text:
    correct_words = word.strip('\n.:;, ')
    print_words.append(correct_words)
print('There are', len(print_words), 'words in the selected text.')


count_title = list()
for word in print_words:
    if word.istitle():
        count_title.append(1)
    else:
        count_title.append(0)
print('There are', sum(count_title), 'titlecase words.')


count_upper = list()
for word in print_words:
    if word.isupper() and not word[0].isnumeric():
        count_upper.append(1)
    else:
        count_upper.append(0)
print('There are', sum(count_upper), 'uppercase words.')


count_lower = list()
for word in print_words:
    if word.islower():
        count_lower.append(1)
    else:
        count_lower.append(0)
print('There are', sum(count_lower), 'lowercase words.')


count_num = list()
for word in print_words:
    if word.isnumeric():
        count_num.append(1)
    else:
        count_num.append(0)
print('There are', sum(count_num), 'numeric strings.')


all_num = list()
for word in print_words:
    if word.isnumeric():
       all_num.append(int(word))
print('The sum of all the numbers',sum (all_num))


print(separator)
print('LEN|       OCCURENCES       |NR.')
print(separator)


counts = dict()
for word in print_words:
    if len(word) in counts:
        counts[len(word)] += 1
    else:
        counts[len(word)] = 1


for LEN, OCCURENCES in sorted(counts.items()):
    if LEN > 9:
        space = 20 - OCCURENCES
        print(LEN, '|', '*' * OCCURENCES,' ' * space, '|',OCCURENCES)
    else:
        space = 20 - OCCURENCES
        print(LEN, ' |', '*' * OCCURENCES, ' ' * space, '|', OCCURENCES)


