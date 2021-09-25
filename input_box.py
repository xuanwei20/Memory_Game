import pygame


class InputBoxCollection:
    """
    Container class to bundle input boxes
    """
    def __init__(self, param1):
        self.screen = param1.screen
        self.font = pygame.font.SysFont("monospace", 25)

        self.input_box1 = InputBox(param1, 200, 100, 235, 32)
        self.input_box2 = InputBox(param1, 200, 150, 235, 32)
        self.input_box3 = InputBox(param1, 200, 200, 235, 32)
        self.input_box4 = InputBox(param1, 200, 250, 235, 32)
        self.input_box5 = InputBox(param1, 200, 300, 235, 32)
        self.input_box6 = InputBox(param1, 200, 350, 235, 32)
        self.input_box7 = InputBox(param1, 200, 400, 235, 32)
        self.input_box8 = InputBox(param1, 200, 450, 235, 32)
        self.input_box9 = InputBox(param1, 200, 500, 235, 32)
        self.input_box10 = InputBox(param1, 200, 550, 235, 32)
        self.input_box11 = InputBox(param1, 580, 100, 235, 32)
        self.input_box12 = InputBox(param1, 580, 150, 235, 32)
        self.input_box13 = InputBox(param1, 580, 200, 235, 32)
        self.input_box14 = InputBox(param1, 580, 250, 235, 32)
        self.input_box15 = InputBox(param1, 580, 300, 235, 32)
        self.input_box16 = InputBox(param1, 580, 350, 235, 32)
        self.input_box17 = InputBox(param1, 580, 400, 235, 32)
        self.input_box18 = InputBox(param1, 580, 450, 235, 32)
        self.input_box19 = InputBox(param1, 580, 500, 235, 32)
        self.input_box20 = InputBox(param1, 580, 550, 235, 32)

        self.input_boxes = [self.input_box1, self.input_box2,
                            self.input_box3, self.input_box4,
                            self.input_box5, self.input_box6,
                            self.input_box7, self.input_box8,
                            self.input_box9, self.input_box10,
                            self.input_box11, self.input_box12,
                            self.input_box13, self.input_box14,
                            self.input_box15, self.input_box16,
                            self.input_box17, self.input_box18,
                            self.input_box19, self.input_box20]

    def check_event(self, event):
        for input_box in self.input_boxes:
            input_box.check_event(event)

    def draw(self):
        for input_box in self.input_boxes:
            input_box.draw()

        self.screen.blit(self.font.render("Enter the names:", 1, (0, 0, 255)), (175, 45))
        self.screen.blit(self.font.render("1", 1, (0, 0, 255)), (175, 100))
        self.screen.blit(self.font.render("2", 1, (0, 0, 255)), (175, 150))
        self.screen.blit(self.font.render("3", 1, (0, 0, 255)), (175, 200))
        self.screen.blit(self.font.render("4", 1, (0, 0, 255)), (175, 250))
        self.screen.blit(self.font.render("5", 1, (0, 0, 255)), (175, 300))
        self.screen.blit(self.font.render("6", 1, (0, 0, 255)), (175, 350))
        self.screen.blit(self.font.render("7", 1, (0, 0, 255)), (175, 400))
        self.screen.blit(self.font.render("8", 1, (0, 0, 255)), (175, 450))
        self.screen.blit(self.font.render("9", 1, (0, 0, 255)), (175, 500))
        self.screen.blit(self.font.render("10", 1, (0, 0, 255)), (165, 550))
        self.screen.blit(self.font.render("11", 1, (0, 0, 255)), (540, 100))
        self.screen.blit(self.font.render("12", 1, (0, 0, 255)), (540, 150))
        self.screen.blit(self.font.render("13", 1, (0, 0, 255)), (540, 200))
        self.screen.blit(self.font.render("14", 1, (0, 0, 255)), (540, 250))
        self.screen.blit(self.font.render("15", 1, (0, 0, 255)), (540, 300))
        self.screen.blit(self.font.render("16", 1, (0, 0, 255)), (540, 350))
        self.screen.blit(self.font.render("17", 1, (0, 0, 255)), (540, 400))
        self.screen.blit(self.font.render("18", 1, (0, 0, 255)), (540, 450))
        self.screen.blit(self.font.render("19", 1, (0, 0, 255)), (540, 500))
        self.screen.blit(self.font.render("20", 1, (0, 0, 255)), (540, 550))


class InputBox:
    def __init__(self, mg_game, x, y, width, height):
        self.screen = mg_game.screen
        self.active = False
        self.input_box = pygame.Rect(x, y, width, height)
        self.input_box_index = 0
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive

        self.clock = pygame.time.Clock()

        # Render the current text.
        self.text = ''
        self.font = pygame.font.SysFont("monospace", 25)
        self.txt_surface = self.font.render(self.text, True, self.color)

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.input_box.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_inactive
        # print(f"active: {self.active}")
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # print(self.text)
                    self.text += "\n"
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    # Render the current text.
                self.txt_surface = self.font.render(self.text, True, self.color)
                # print(f"self.text: {self.text}")

    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.input_box.x + 5, self.input_box.y + 5))

        # Blit the input_box rect.
        pygame.draw.rect(self.screen, self.color, self.input_box, 2)
