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

# Paths
music_path = './Asset/Music/'
menu_path = './Asset/Menu/'

# Speed
entity_speed = {
    'Level1': 0,
    'Level2': 1,
    'Character': 4,
    'Obstacle1': 3,
    'Obstacle2': 3,
}

# Obstacle

event_obstacle = pygame.USEREVENT + 1

# Spawn
spawn_time = 5000