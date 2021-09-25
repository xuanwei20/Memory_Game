import pygame


class MemoryPalace:
    """A class to manage background image."""

    def __init__(self, mg_game):
        """Initialize the background and set its starting position."""
        self.mg_game = mg_game

        # Variables to manage the background change
        self.image_time = pygame.time.get_ticks() - self.mg_game.settings.game_active_start_time

        self.image_index = 0  # index of the currently used background
        self.rect_index = 0
        self.never_set = True

        # Load the images and get its rect.
        self.image1 = pygame.image.load('images/house.bmp')
        self.rect1 = self.image1.get_rect()
        self.rect1.center = self.mg_game.screen_rect.center
        self.image2 = pygame.image.load('images/kitchen.bmp')
        self.rect2 = self.image2.get_rect()
        self.rect2.center = self.mg_game.screen_rect.center
        self.image3 = pygame.image.load('images/livingroom1.bmp')
        self.rect3 = self.image3.get_rect()
        self.rect3.center = self.mg_game.screen_rect.center
        self.image4 = pygame.image.load('images/studyroom.bmp')
        self.rect4 = self.image4.get_rect()
        self.rect4.center = self.mg_game.screen_rect.center
        self.image5 = pygame.image.load('images/bathroom1.bmp')
        self.rect5 = self.image5.get_rect()
        self.rect5.center = self.mg_game.screen_rect.center
        self.image6 = pygame.image.load('images/livingroom.bmp')
        self.rect6 = self.image6.get_rect()
        self.rect6.center = self.mg_game.screen_rect.center
        self.image7 = pygame.image.load('images/bedroom2.bmp')
        self.rect7 = self.image7.get_rect()
        self.rect7.center = self.mg_game.screen_rect.center
        self.image8 = pygame.image.load('images/bedroom1.bmp')
        self.rect8 = self.image8.get_rect()
        self.rect8.center = self.mg_game.screen_rect.center
        self.image9 = pygame.image.load('images/bathroom.bmp')
        self.rect9 = self.image9.get_rect()
        self.rect9.center = self.mg_game.screen_rect.center

        self.images = [self.image1, self.image2, self.image3,
                       self.image4, self.image5, self.image6,
                       self.image7, self.image8, self.image9]

        self.rect = [self.rect1, self.rect2, self.rect3,
                     self.rect4, self.rect5, self.rect6,
                     self.rect7, self.rect8, self.rect9]

        self.image_delays = [self.mg_game.settings.image_delay1, self.mg_game.settings.image_delay2,
                             self.mg_game.settings.image_delay3, self.mg_game.settings.image_delay4,
                             self.mg_game.settings.image_delay5, self.mg_game.settings.image_delay6,
                             self.mg_game.settings.image_delay7, self.mg_game.settings.image_delay8,
                             self.mg_game.settings.image_delay9]

        self.current_image_delay = self.image_delays[self.image_index]
        self.mg_game.show_time.counter = int(self.image_delays[self.image_index] / 1000)
        self.mg_game.show_time.text = str(self.mg_game.show_time.counter).rjust(1)

    def blitme(self):
        """Draw the image nad its current location."""
        time_now = pygame.time.get_ticks() - self.mg_game.settings.game_active_start_time

        if self.image_index >= (len(self.images) - 1):
            self.mg_game.settings.solution_entry = True
        else:
            # Draw the image
            self.mg_game.screen.blit(self.images[self.image_index], self.rect[self.rect_index])

            if time_now > self.image_time + self.current_image_delay:
                print(f"image_index = {self.image_index}, current_image_delay = {self.current_image_delay}")
                # switch to the next picture
                self.image_index += 1
                self.rect_index += 1
                self.current_image_delay = self.image_delays[self.image_index]
                self.mg_game.show_time.counter = int(self.image_delays[self.image_index] / 1000)
                self.mg_game.show_time.text = str(self.mg_game.show_time.counter).rjust(1)
                print(f"2 image_index = {self.image_index}, current_image_delay = {self.current_image_delay}")
                self.image_time = time_now
