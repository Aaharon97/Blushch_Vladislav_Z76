import re
print('Введите предложение из двух слов:')
s = ' '.join(input( ).split(' ')[::-1])
s1 = s.replace(" "," ! ")
s2 = re.sub(r'[ ]',' ! ', s)
print('!' + s1 + '!')
print('!' + s2 + '!')
