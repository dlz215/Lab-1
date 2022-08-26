name = input('What is your name? ')
birth_month = input('What month were you born in? ')

print('Hello, ' + name)
print(f'Hello, {name}! Great to meet you')

letters_in_name = len(name)
print(f'You have {letters_in_name} letters in your name')

if birth_month.lower() == 'august':
    print('Happy birthday month')
elif birth_month.lower() == 'september':
    print('It is your birthday next month')
else:
    print('')

classes = input ('Please enter your classes seperated by a comma: ')
class_list = classes.split(', ')
for x in class_list:
    print(x)

sentence = input('Enter a sentence: ')
words_list = sentence.split(' ')
for word in words_list:
    word.lower()
    string = word
    letters = [letter for letter in word]
    letters[0] = letters[0].upper()
    print[letters]





