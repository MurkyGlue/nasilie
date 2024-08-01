rus = '''йцукенгшщзъхэждлорпавыфячсмитьбюёЙЦУКЕНГШЩЗЪХЭЖДЛОРПАВЫФЯЧСМИТЬБЮЁ .,1234567890-=!"№;%:?*()_+\|'''
eng = '''qwertyuiop][';lkjhgfdsazxcvbnm,.`QWERTYUIOP}{":LKJHGFDSAZXCVBNM<>~ /?1234567890-=!@#$%^&*()_+\|'''
st2 = ''''''
st1 = input('введите текст\n')
if rus.find(st1[0]) == -1:
    for i in range(len(st1)):st2 += rus[eng.find(st1[i])]
else:
    for i in range(len(st1)):st2 += eng[rus.find(st1[i])]
print(st2)