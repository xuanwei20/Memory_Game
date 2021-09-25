class Settings:
    """A class to store all settings for Memory Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1350
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        self.game_active = False
        self.game_active_start_time = 0
        self.solution_entry = False
        self.grade_answer = False

        self.image_delay1 = 30000  # milliseconds
        self.image_delay2 = 10000
        self.image_delay3 = 10000
        self.image_delay4 = 10000
        self.image_delay5 = 10000
        self.image_delay6 = 10000
        self.image_delay7 = 10000
        self.image_delay8 = 10000
        self.image_delay9 = 10000
