import sys
import pygame

from settings import Settings
from instruction_image import InstructionImage
from button import PlayButton, SubmitButton
from memory_palace import MemoryPalace
from show_time import ShowTime
from input_box import InputBoxCollection
from scoreboard import ScoreBoard


class MemoryGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Full Screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Memory Game")
        self.screen_rect = self.screen.get_rect()

        self.instruction_image = InstructionImage(self)
        self.show_time = ShowTime(self)
        self.memory_palace = MemoryPalace(self)

        # Make the play button
        self.play_button = PlayButton(self, "Play")
        self.submit_button = SubmitButton(self, "Submit")
        self.clock = pygame.time.Clock()

        self.input = InputBoxCollection(self)
        self.scoreboard = ScoreBoard(self)
        self.total_score = 0

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypress and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            if self.settings.game_active is False and \
                    self.settings.solution_entry is False:
                # Start screen is running
                self.play_button.check_event_button(event)

            if self.settings.game_active is True:
                # Pictures to memorize are running
                self.show_time.process_event(event)

            if self.settings.solution_entry is True:
                # User entry is running
                self.input.check_event(event)
                self.submit_button.check_event_button(event)

    def _update_screen(self):
        # Update the images on the screen, and flip to new screen.
        self.screen.fill(self.settings.bg_color)

        # Draw the play button if the game is inactive.
        if not self.settings.game_active:
            self.instruction_image.blitme()
            self.play_button.draw_button()
        else:
            self.memory_palace.blitme()
            if self.settings.solution_entry is False:
                self.show_time.show_time()
            if self.settings.solution_entry is True:
                self.input.draw()
                self.submit_button.draw_button()
            if self.settings.grade_answer is True:
                self.scoreboard.show_score(self.total_score)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    mg = MemoryGame()
    mg.run_game()
