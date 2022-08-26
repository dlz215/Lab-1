#PART 
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
    print('Your birthday is not this month or next month')

#PART 2
classes = input ('Please enter your classes separated by a comma: ')
class_list = classes.split(',')
for x in class_list:
    x = x.strip()
    print(x)

#PART 3
camelcase = ''

sentence = input('Enter a sentence: ')

word_list = sentence.split(' ')

for word in word_list:
    # for any word in the list other than the first, break it up into a list of individual letters
    if word_list.index(word) != 0:
        captialized_word = ''
        word = word.lower()
        letters = [letter for letter in word]
        # capitalize the first letter in the list
        letters[0] = letters[0].upper()
        # put the capitalized word back together and append to the final camelcase string
        for letter in letters:
            captialized_word = captialized_word + letter
        camelcase = camelcase + captialized_word
   
    # for the first word in the list, simply add it to the final camelcase string
    else:
        word = word.lower()
        camelcase = camelcase + word

print(camelcase)


            




        


  

        





    






