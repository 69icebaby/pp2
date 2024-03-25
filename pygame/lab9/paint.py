import pygame

pygame.init()


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue_green = (182, 242, 114)
icon_rectangle_tab_color = (255, 0, 0)


dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Paint')

clock = pygame.time.Clock()

elements_to_draw = []


def drawShapes(mainscreen):
    for element in elements_to_draw:
        if element['shape'] == 'SQUARE':
            pygame.draw.rect(mainscreen, element['color'],
                             (element['x'], element['y'], 40, 40))
        elif element['shape'] == 'CIRCLE':
            pygame.draw.circle(mainscreen, element['color'],
                               (element['x'], element['y']), 20)
        elif element['shape'] == 'TRIANGLE':
            pygame.draw.polygon(mainscreen, element['color'],
                                [(element['x'], element['y']),
                                 (element['x'] + 20, element['y'] + 40),
                                 (element['x'] - 20, element['y'] + 40)])


def drawMainIcons(mainscreen):
    pygame.draw.circle(mainscreen, green, (30, 90), 20)
    pygame.draw.polygon(mainscreen, blue_green,
                        [(30, 150), (50, 200), (10, 200)])
    pygame.draw.rect(mainscreen, icon_rectangle_tab_color,
                     [5, 5, 40, 30])


def game_loop():
    game_over = False
    position = (0, 0)
    pygame.draw.rect(dis, white, [0, 0, dis_width, dis_height])

    is_rectangle_drawer = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if position[0] < 50 and position[1] < 50:
                        print('rectangle chosen')
                        is_rectangle_drawer = True
                    else:
                        if is_rectangle_drawer:
                            print('draw rectangle')
                            elements_to_draw.append({
                                'shape': 'SQUARE',
                                'color': blue_green,
                                'x': position[0],
                                'y': position[1]
                            })
                        else:
                            print('draw circle')
                            elements_to_draw.append({
                                'shape': 'CIRCLE',
                                'color': green,
                                'x': position[0],
                                'y': position[1]
                            })
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                print(position)

        dis.fill(white)
        drawShapes(dis)
        drawMainIcons(dis)
        pygame.display.update()
        clock.tick(60)


game_loop()