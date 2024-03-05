import random

width, height = 800, 600
def singleplayer():
    ball_size = 20
    ball_speed = 5
    ball_direction = [random.choice([-1,1]), random.choice([-1,1])]
    ball_position = [width // 2, height //2] 

