from CellModel import *

def step_maps(step, symbol):
    index = maps.index(step)
    maps[index] = symbol

maps = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_result():
    win = ""

    for i in successful_variations:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win


successful_variations = [[0, 1, 2], [3, 4, 5], [0, 4, 8], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6]]

# Основная программа
game_over = False
player1 = True

while game_over == False:

    pygame.init()
    sc = pygame.display.set_mode((740, 770))
    pygame.display.set_caption("Крестики да нолики")

    cell_image = pygame.image.load('1.png')
    cells = []

    for i in range(3):
        cell_row = []
        for j in range(3):
            current_x = 35 + 225 * j
            current_y = 35 + 240 * i
            current_cell = Cell(current_x, current_y, cell_image)
            cell_row.append(current_cell)
        cells.append(cell_row)

    pygame.display.flip()
    pygame.display.update()

    running = True
    sum = 0

    while (running):

        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            x, y = pygame.mouse.get_pos()
            hover_cell = None
            click_cell = None

            for i in range(3):
                for j in range(3):

                    current_cell = cells[i][j]
                    if current_cell.point_inside(x, y):
                        hover_cell = current_cell
                        cells[i][j].hover_now = True

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            click_cell = current_cell
                            cells[i][j].click_now = True
                            cells[i][j].Value = (j + 1) + 3 * i
                            sum=sum+1

                            if player1 == True:
                                symbol = "X"
                                cells[i][j].Value_two = "X"
                                step = cells[i][j].Value
                            else:
                                symbol = "O"
                                cells[i][j].Value_two = "O"
                                step = cells[i][j].Value

                            step_maps(step, symbol)
                            win = get_result()
                            if win != "":
                                game_over = True
                                print("Победил", win)
                            else:
                                if sum==9:
                                    game_over = True
                                    print("Ничья")
                                game_over = False

                            player1 = not (player1)

                        else:
                            cells[i][j].click_now = False

                    else:
                        cells[i][j].hover_now = False

            cell_drawer.draw_background(sc)
            for i in range(3):
                for j in range(3):
                    current_cell = cells[i][j]
                    cell_drawer.draw_cell(sc, current_cell)

            if game_over == True:
                if win == "O":
                    sc.blit(pygame.image.load('win_O.png'), (0, 0))
                else:
                    if win == "X":
                        sc.blit(pygame.image.load('win_X.png'), (0, 0))
                    else:
                        sc.blit(pygame.image.load('win_nobody.png'), (0, 0))
        pygame.display.update()

