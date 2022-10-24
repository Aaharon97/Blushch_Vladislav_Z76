import  re
s =  input()
s1 = re.sub(r'[-]','', s)
s2 = re.sub(r'[.]','', s)
s3 = re.sub(r'[.]','', s1)
def check_number(s):
    if s.isdigit():
        print(f'целое положительное число {s}')
    elif s1.isdigit():
        print(f'отрицательное число {s}')
    elif s2.isdigit():
        print(f'положительное дробное число {s}')
    elif s3.isdigit():
        print(f'отрицательное дробное число {s}')
    else:
        print(f'не корректное число {s}')

check_number(s)







