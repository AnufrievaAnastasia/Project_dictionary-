menu = input('Введите номер пункта:\n'
             '1. Общий актерский состав, снимавшийся хотя бы в одном из этих двух фильмов.\n'
             '2. Актеры, снимавшиеся и в первом, и во втором фильме.\n'
             '3. Актеры, участвующие в съемках первого, но не участвующих в съемках второго.\n'
             '4. Названия фильмов, в которых снимался хотя бы в одном из актеров (названия фильмов повторяться '
             'не должны).\n'
             '5. Определить названия фильмов, в которых снимались оба актера.\n'
             '6. Определить названия фильмов, в которых снимался первый актер, но не участвовал в съемках второй.\n')

with open('info.txt') as info:
    information = {}
    for line in info:
        name_start = line.find('Название фильма:')
        actors_start = line.find('Актерский состав:')
        list_actors = set(line[actors_start + 18:len(line) - 1].split(', '))
        key_name = line[name_start + 17:actors_start-1]
        information[key_name] = list_actors

information_2 = str(information)

n = information_2[1:len(information_2) - 1].replace('{', '[')
n = n.replace('}', ']')
result_n = '{' + n + '}'
information_result = eval(result_n)

newdict = {}

for i in information_result.keys():
    for p in information_result.get(i):
        newdict.setdefault(p, []).append(i)

if menu in '123':
    film1 = input('Введите название первого фильма: ')
    film2 = input('Введите название второго фильма: ')
    if menu == '1':
        print(*(set(information[film1]) | set(information[film2])))
    elif menu == '2':
        print(*(set(information[film1]) & set(information[film2])))
    elif menu == '3':
        print(*(set(information[film1]) - set(information[film2])))


else:
    name1 = input('Введите имя первого актера: ')
    name2 = input('Введите имя второго актера: ')
    if menu == '4':
        print(*(set(newdict[name2]) | set(newdict[name1])))
    elif menu == '5':
        print(*(set(newdict[name2]) & set(newdict[name1])))
    elif menu == '6':
        print(*(set(newdict[name2]) - set(newdict[name1])))

print(newdict)