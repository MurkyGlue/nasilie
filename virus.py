import random
sym = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъэждлорпавыфячсмитьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ!@#$%^&*_+=-?/'
lim = 50
while True:
	name, pas = '', ''
	for i in range(random.randint(1, lim)):name += sym[random.randint(0, len(sym)-1)]
	for i in range(random.randint(1, lim)):pas += sym[random.randint(0, len(sym)-1)]
	file = open(f'{name}.txt', 'w+')
	file.write(pas)
	file.close()