import pygame
class Cell:
    def __init__(self, x, y, image):
        self.Value = None
        self.Value_two = None
        self.hover_now = False
        self.click_now = False
        self.X = x
        self.Y = y
        self.Image = image


    def point_inside(self, x, y):
        return self.X <= x <= self.Image.get_width() + self.X \
                and \
                self.Y <= y <= self.Image.get_height() + self.Y - 70 #вынести константу


class cell_drawer:
    @staticmethod
    def draw_cell(screen, cell):
        if cell.hover_now == False:
            screen.blit(cell.Image, (cell.X, cell.Y))
        else:
            if cell.click_now == False and cell.Value == None:
                screen.blit(cell.Image, (cell.X, cell.Y-30)) #вынести константу
            else:
                screen.blit(cell.Image, (cell.X, cell.Y))
                if cell.Value_two == "O":
                    screen.blit(pygame.image.load('O.png'), (cell.X, cell.Y))
                else:
                    screen.blit(pygame.image.load('X.png'), (cell.X, cell.Y))

        if cell.Value != None:
            if cell.Value_two == "O":
                screen.blit(pygame.image.load('O.png'), (cell.X, cell.Y))
            else:
                screen.blit(pygame.image.load('X.png'), (cell.X, cell.Y))



    @staticmethod
    def draw_background(screen):
        screen.fill((70, 131, 94))

