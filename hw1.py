# Задание №1.
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
# Ввод:

# пара-ра-рам рам-пам-папам па-ра-па-да

# Вывод:
# Парам пам-пам



def checking_vowel(phrase):
    sum=0
    alph=set('АЕЁИЙОУЫЭЮ')
    for j in range(len(phrase)):
        if phrase[j] in alph: 
            sum+=1   
    return sum


def all_same(elements):
    if len(elements) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')


fraza_vinni=set(input('Введите фразу Винни-Пуха: ').upper().split(" ") )
all_same(set(map(checking_vowel,fraza_vinni)))








