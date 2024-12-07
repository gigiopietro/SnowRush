import pygame

# Colors
lilac_color=(119, 103, 206)
white_color=(255, 255, 255)
yellow_color=(253, 253, 150)

# Menu options
option_menu=('New Game', 'Score', 'Exit')

# Size
display_width=576
display_height=324

# Position
score_pos ={'Title': (display_width / 2, 50),
            'EnterName': (display_width/ 2, 90),
            'Label': (display_width / 2, 110),
            'Nickname': (display_width / 2, 120),
            'Label2':(display_width / 2, 160),
            0: (display_width / 2, 130),
            1: (display_width / 2, 150),
            2: (display_width / 2, 170),
            3: (display_width / 2, 190),
            4: (display_width / 2, 210),
            5: (display_width / 2, 230),
}

# Paths
music_path = './Asset/Music/'
menu_path = './Asset/Menu/'
score_path = './Asset/Background/'

# Speed
entity_speed = {
    'lvl1_1': 3,
    'lvl1_2': 3,
    'lvl1_3': 3,
    'lvl1_4': 3,
    'lvl1_5': 3,
    'bg_Ground': 5,
    'Character': 4,
    'Obstacle1': 6,
    'Obstacle2': 7,
}

# Obstacle

event_obstacle = pygame.USEREVENT + 1

# Spawn
spawn_time = 5000

# Health
entity_health = {'lvl1_1': 999,
                 'lvl1_2': 999,
                 'lvl1_3': 999,
                 'lvl1_4': 999,
                 'lvl1_5': 999,
                 'bg_Ground': 999,
                 'Character': 300 ,
                 'Obstacle1': 10,
                 'Obstacle2':  10,
}

