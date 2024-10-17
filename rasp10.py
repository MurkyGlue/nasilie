import time, pygame
pygame.font.init()
sc = pygame.display.set_mode((1080, 2340))

lessons = [
    ["Разговоры о важном  105", "Английский  310", "Русский язык  301", "Алгебра  303", "Геометрия  303", "История  308", "Физ-ра", "Литература  113"],
    ["Физика  209", "Физика  209", "Алгебра  303", "Геометрия  303", "Обществознание  308", "Литература  113", "Информатика  208"],
    ["", "Биология  309", "Химия  306", "Физика  209", "Физика  209", "Литература  113", "История  308", "Английский  310"],
    ["Разговоры о важном  105", "Русский  301", "ВиС  209", "Алгебра  303", "Физика  209", "Физика  209", "География  317"],
    ["Проект  206", "Обществознание  308", "ОБЖ  319", "Алгебра  303", "Геометрия  303", "Физ-ра", "Английский  310"],
    [],
    []
]
bells = [
    [8.05, 8.55, 9.50, 10.45, 11.45, 12.45, 13.35, 14.25, 15.15],
    [8.45, 9.35, 10.30, 11.25, 12.25, 13.25, 14.15, 15.05, 15.55]
]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
pos = [0, 150, 300, 450, 600, 750, 900, 1050]
les = [pygame.font.SysFont("Adobe Gothic Std Kalin", 100), 
       pygame.font.SysFont("Adobe Gothic Std Kalin", 100), 
       pygame.font.SysFont("Adobe Gothic Std Kalin", 100), 
       pygame.font.SysFont("Adobe Gothic Std Kalin", 100), 
       pygame.font.SysFont("Adobe Gothic Std Kalin", 100), 
       pygame.font.SysFont("Adobe Gothic Std Kalin", 100), 
       pygame.font.SysFont("Adobe Gothic Std Kalin", 100), 
       pygame.font.SysFont("Adobe Gothic Std Kalin", 100)]
c = 10
pygame.init()
while True:
    sc.fill((40, 40, 40))
    t = time.asctime(time.localtime(time.time()))
    
    hm = int(t[11:13]) + float(t[14:16])/100
    day = days.index(t[0:3])
    if hm > 18:
        hm = 0.0
        if day < 6:day = days.index(t[0:3])+1
        else:day = 0
    for i in range(len(bells[0])):
        if bells[0][i] <= hm <= bells[1][i]:check = True;break
        else:check = False
    for i in range(len(lessons[day])):
        if hm <= bells[1][i]:c = i;break
    for i in range(len(lessons[day])-c):
        if check:pygame.draw.rect(sc, (0, 120, 0), [0, 0, 1080, 150]);check = False
        sc.blit(les[i].render(lessons[day][i+c], True, (255, 255, 255)), [80, pos[i]+40])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()