newfile = open('print.txt', 'x')
two_words = input('Please type any two words: ')
print(two_words.split(' ')[0], two_words.split(' ')[-1], sep='<<<>>>', file=newfile)
first_word = two_words.split(' ')[0]
second_word = two_words.split(' ')[-1]


format_1 = '!%s %s?' % (second_word.title(), first_word.upper())
print(format_1)
print('!', second_word.title(), first_word.upper(), '?', sep='<<<>>>', file=newfile)
format_2 = '!{} {}?'.format(second_word.title(), first_word.upper())
print(format_2)
print('!', second_word.title(), first_word.upper(), '?', sep='<<<>>>', file=newfile)
format_3 = f'!{second_word.title()} {first_word.upper()}?'
print(format_3)
print('!', second_word.title(), first_word.upper(), '?', sep='<<<>>>', file=newfile)

