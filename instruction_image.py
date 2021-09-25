import pygame


class InstructionImage:
    """A class to manage image."""

    def __init__(self, mg_game):
        """Initialize the image and set its starting position."""
        self.mg_game = mg_game

        # Load the image and get its rect.
        self.image = pygame.image.load('images/game_instruction.bmp')
        self.rect = self.image.get_rect()

        # Start each new image at the center of the screen.
        self.rect.center = self.mg_game.screen_rect.center

    def blitme(self):
        """Draw the image nad its current location."""
        self.mg_game.screen.blit(self.image, self.rect)

