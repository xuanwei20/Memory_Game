import pygame.font


class Button:

    def __init__(self, mg_game, msg):
        """Initialize button attributes."""
        self.mg_game = mg_game
        self.screen = mg_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimension and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 130)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and display it at the bottom right of the screen.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.bottomright = self.screen_rect.bottomright

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def check_event_button(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_clicked = self.rect.collidepoint(mouse_pos)
            if button_clicked:
                # Mouse click occurred
                self._button_click_action()

    def _button_click_action(self):
        pass

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class PlayButton(Button):
    def _button_click_action(self):
        """Start a new game when the player clicks play."""
        if not self.mg_game.settings.game_active:
            self.mg_game.settings.game_active = True
            self.mg_game.settings.game_active_start_time = pygame.time.get_ticks()


class SubmitButton(Button):
    def _button_click_action(self):
        """Submit answers."""
        if self.mg_game.settings.grade_answer is False:
            self.mg_game.settings.grade_answer = True
            self.mg_game.total_score = self.mg_game.scoreboard.check_answer()
