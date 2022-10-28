import random

tel_dect = {}
man_dect = {}
woman_dect = {}
prof_dect = {}
with open("E:/IT_HomeWork/name.txt", 'r', encoding='utf-8') as mn:
    man_name = mn.read().splitlines()
with open("E:/IT_HomeWork/wname.txt", 'r', encoding='utf-8') as wn:
    woman_name = wn.read().splitlines()
with open("E:/IT_HomeWork/msern.txt",'r', encoding='utf-8') as ms:
    man_sern = ms.read().splitlines()
with open ("E:/IT_HomeWork/proff.txt",'r', encoding='utf-8') as prof:
    prof_all = prof.read().splitlines()
for i in range(1, 501): 
    man_dect[i] = {'surname' : man_sern[random.randint(0,96)], 'name' : man_name[random.randint(0,99)], 'prof' : prof_all[random.randint(0,249)]}
    woman_dect[i] = {'surname' : man_sern[random.randint(0,96)] + 'a', 'name' : woman_name[random.randint(0,99)], 'prof' : prof_all[random.randint(0,249)]}
# print(man_dect, woman_dect)
    
for i in range(1, 501):
    a = random.randint(1,10)
    if a%3 != 0:
        tel_dect[i] = {'idd':i,'surname': man_dect[i]['surname'], 'name': man_dect[i]['name'],
        'telefon' : f'+7({random.randint(900, 999)})-{random.randint(100,999)}-{random.randint(10, 99)}-{random.randint(10, 99)}'
        , 'status': man_dect[i]['prof']}
    else:
        tel_dect[i] = {'idd':i,'surname': woman_dect[i]['surname'], 'name': woman_dect[i]['name'],
        'telefon' : f'+7({random.randint(900, 999)})-{random.randint(100,999)}-{random.randint(10, 99)}-{random.randint(10, 99)}',
        'status': man_dect[i]['prof']}
f = open('E:/IT_HomeWork/tel.txt', 'w', encoding='utf-8')
# f.write('id surname name  telefon \n')
for i in range(1, 501):
    f.write(str(tel_dect[i]['idd']) + '  ')
    f.write(tel_dect[i]['surname'] + ' ')
    f.write(tel_dect[i]['name']+ ' ')
    f.write(tel_dect[i]['telefon'] + ' ')
    f.write(tel_dect[i]['status'] + '\n')
    # print(tel_dect[i]['name'], tel_dect[i]['surname'], tel_dect[i]['telefon'])
f.close()

''' 
# with open("msern.txt", "r") as ms:
#     woman_sern = ms.read().splitlines()  
 # woman_sern = ['Иванова', "Петрова", "Сидорова", "Картаева", "Нечаева", "Щербакова", "Попова", "Пономарева"]
# for i in range(2, 100, 2):
#     tel_dect[i] = {'idd':i, 'surname': man_sern[random.randint(0,90)], 'name': man_name[random.randint(0,99)], 'telefon' : f'+7({random.randint(900, 999)})-{random.randint(100,999)}-{random.randint(10, 99)}-{random.randint(10, 99)}'}
#print(tel_dect)
# woman_name = ['Екатерина', "Ольга", "Татьяна", "Кристина", "Наталья", "Оксана", "Мария", "Светлана"]
'''

