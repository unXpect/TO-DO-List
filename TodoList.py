from datetime import date


f = open(f'{date.today()}.txt', 'w')
f.write('-----TO-DO List-----' + '\n')

while True:
    b = input('Введите свои дела:')
    if b.lower() == 'stop':
        print('Данные записаны в файл')
        break
    else:
        f.write(b + '\n')
        
f.write('----------')
