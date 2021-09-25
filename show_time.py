import pygame


class ShowTime:

    def __init__(self, mg_game):
        self.screen = mg_game.screen
        self.clock = pygame.time.Clock()

        self.counter = 0
        self.text = str(self.counter).rjust(1)

        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font = pygame.font.SysFont(None, 50)

    def process_event(self, event):
        if event.type == pygame.USEREVENT:
            self.counter -= 1
            self.text = str(self.counter).rjust(1) if self.counter > 0 else 'Next!'

    def show_time(self):
        self.screen.blit(self.font.render(self.text, True, (0, 0, 255)), (10, 10))


