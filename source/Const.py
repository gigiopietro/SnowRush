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
            'EnterName': (display_width/ 2, 80),
            'Label': (display_width / 2, 90),
            'Name': (display_width / 2, 110),
            0: (display_width / 2, 110),
            1: (display_width / 2, 130),
            2: (display_width / 2, 150),
            3: (display_width / 2, 170),
            4: (display_width / 2, 190),
            5: (display_width / 2, 210),

}

# Paths
music_path = './Asset/Music/'
menu_path = './Asset/Menu/'
score_path = './Asset/Background/'

# Speed
entity_speed = {
    'Level1': 0,
    'Level2': 1,
    'Character': 4,
    'Obstacle1': 3,
    'Obstacle2': 5,
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
                 'lvl1_5': 999 ,
                 'bg_losangcompleto':999,
                 'Character': 300 ,
                 'Obstacle1': 10,
                 'Obstacle2':  10,
}

