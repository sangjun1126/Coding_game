# ursina 모듈 사용하기
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
mouse.visible = False

main_floor = Entity(model = "cube", position=(0,0,0), scale = (10,1,100), color = color.gray, collider='box')
main_ceiling = Entity(model = "cube", position=(0,10,0), scale = (10,1,100), color = color.gray, collider='box')
main_left_wall = Entity(model = "cube", position=(-5,5,-5), scale = (10,1,110), color = color.white,
collider='box', texture = 'assets/wall.jpg')
main_right_wall = Entity(model = "cube", position=(5,5,5), scale = (10,1,110), color = color.white, 
collider='box', texture = 'assets/wall.jpg')
# EditorCamera()

# 1인칭 시점으로 플레이 하기
player = FirstPersonController()
player.cursor.visible = False
player.gravity = 0.5
player.speed = 0.5

app.run()