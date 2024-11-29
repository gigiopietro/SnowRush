import pygame.image
music_path = './Asset/Music/'
menu_path = './Asset/Menu/'

class Menu:
    def __init__(self, window):
        self.window=window
        self.bgMenu = pygame.image.load(menu_path + 'PRE_ORIG_SIZE.png')
        self.rect = self.bgMenu.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load(music_path + 'MenuMusic.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.bgMenu, dest=self.rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()