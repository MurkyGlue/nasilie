from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController 

app = Ursina()

player = FirstPersonController()
player.gravity = 0
player.position = Vec3(5, 0, 5)

for i in range(6):
    for j in range(3):
        for k in range(3):
            if i == 0:
                Entity(model = 'cube', color = color.red, position = (j, -1, k))
            elif i == 1:
                Entity(model = 'cube', color = color.blue, position = (-1, j, k))
            elif i == 2:
                Entity(model = 'cube', color = color.green, position = (3, j, k))
            elif i == 3:
                Entity(model = 'cube', color = color.yellow, position = (k, j, -1))
            elif i == 4:
                Entity(model = 'cube', color = color.white, position = (k, j, 3))
            elif i == 5:
                Entity(model = 'cube', color = color.orange, position = (k, 3, j))




app.run()