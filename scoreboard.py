import pygame


class ScoreBoard:
    def __init__(self, mg_game):
        self.mg_game = mg_game
        self.screen = mg_game.screen
        self.settings = mg_game.settings
        self.correct_answers = ["Rapunzel",
                                "Simba",
                                "Shrek",
                                "Pinocchio",
                                "Dumbo",
                                "Porky Pig",
                                "Sponge Bob",
                                "Cinderella",
                                "Ariel",
                                "Jasmine",
                                "Blossom",
                                "Peppa Pig",
                                "Doraemon",
                                "Popeye",
                                "Tweety",
                                "Homer Simpson",
                                "Peter Griffin",
                                "Genie",
                                "Patrick Star",
                                "Baby Pluto",
                                ]

    def check_answer(self):
        points = 0
        answers = []
        for input_box_number in range(len(self.mg_game.input.input_boxes)):
            answers.append(self.mg_game.input.input_boxes[input_box_number].text)

        for correct_answer, answer in zip(self.correct_answers, answers):
            if correct_answer == answer.title():
                points += 1

        return points

    """
        ToDo:
        answers = self.mg_game.input.text.split('\n')
        for self.correct_answer, answer in zip(self.correct_answers, answers):
            if self.correct_answer == answer.title():
                points += 1
        return points
    """

    def show_score(self, score):
        # Font settings for scoring information.
        text_color = (0, 0, 230)
        font = pygame.font.Font(None, 80)
        text = font.render(f"You got {score} points!", True, text_color)
        text_rect = text.get_rect()
        text_rect.center = (855, 545)
        self.screen.blit(text, text_rect.center)
