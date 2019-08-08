import pygame
import sys

W_WIDTH = 500
W_HEIGHT = 500

screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
screen_rect = screen.get_rect()


class MessageBox:
    def __init__(self, window_rect, font, message, charname):
        self.window_rect = window_rect
        self.font = font
        self.background_colour = pygame.Color("#d9d4cc")
        self.name_colour = pygame.Color("#4a3b23")
        self.text_colour = pygame.Color("#000000")


        self.window_title_str = charname
        self.title_text_render = self.font.render(self.window_title_str, True, self.name_colour)

        self.should_exit = 0

        self.done_button = UTTextButton([self.window_rect[0] + (self.window_rect[2] / 2) + 150,
                                         self.window_rect[1] + self.window_rect[3] - 30, 70, 20], "Done", font)

        self.message = message
        self.message_text_render = self.font.render(self.message, True, self.text_colour)

    def handle_input_event(self, event):
        self.done_button.handle_input_event(event)

    def update(self):
        self.done_button.update()

        if self.done_button.was_pressed():
            self.should_exit = self.should_exit + 1

    def is_inside(self, screen_pos):
        is_inside = False
        if self.window_rect[0] <= screen_pos[0] <= self.window_rect[0] + self.window_rect[2]:
            if self.window_rect[1] <= screen_pos[1] <= self.window_rect[1] + self.window_rect[3]:
                is_inside = True
        return is_inside

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_colour, pygame.Rect(self.window_rect[0], self.window_rect[1],
                                                                     self.window_rect[2], self.window_rect[3]), 0)

        screen.blit(self.title_text_render,
                    self.title_text_render.get_rect(centerx=self.window_rect[0] + self.window_rect[2] * 0.125,
                                                    centery=self.window_rect[1] + 20))

        screen.blit(self.message_text_render,
                    self.message_text_render.get_rect(centerx=self.window_rect.centerx,
                                                      centery=self.window_rect[1] + 60))

        self.done_button.draw(screen)


class UTTextButton:
    def __init__(self, rect, text, font):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.text_colour = pygame.Color("#FFFFFF")
        self.background_colour = pygame.Color("#151515")
        self.text_render = self.font.render(self.text, True, self.text_colour)
        self.text_rect = self.text_render.get_rect()
        self.text_rect.center = self.rect.center

    def update(self):
        pass

    def was_pressed(self):
        MOUSEPRESSED = pygame.mouse.get_pressed() # Get Keyboard Input
        mpos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mpos) and MOUSEPRESSED:
            return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_colour, self.rect)
        screen.blit(self.text_render, self.text_rect)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image = pygame.image.load(self.image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (53,77))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = pos

class npc(pygame.sprite.Sprite):
    def __init__(self, pos, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.pos = pos
        self.image = pygame.image.load(self.image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,127))
        self.rect = self.image.get_rect()

        self.rect.center = pos

def dialogue(text, name):
    screen_rect = screen.get_rect()
    window_rect = pygame.Rect(0, 0, 500, 150)
    window_rect.bottom = screen_rect.bottom
    font = pygame.font.SysFont('lucidaconsole', 14)
    name = name
    i = 0

    message =text[i]
    box = MessageBox(window_rect, font, message,name)
    h = 0
    text_len = len(text)

    running = True
    while running:
#        clock.tick(60)
        #clock = pygame.time.Clock()

        #fps = 50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                MOUSEPRESSED = True
                i = i + 1
                message = text[i]
                box = MessageBox(window_rect, font, message, name)
                h = h + 1

        box.update()
        #screen.fill((0, 0, 0))
        box.should_exit = h
        if box.should_exit < text_len-1:
            box.draw(screen)
        else:
            pygame.display.flip()
            break
        #box.draw(screen)
        pygame.display.flip()
        #clock.tick(fps)
    #pygame.display.update()


def check_npc(bol,loc_x, loc_y, pic, screen, group):
    if bol==True:
        group.empty()
        mob = npc([loc_x,loc_y], pic)
        group = pygame.sprite.Group()
        group.add(mob)
        group.draw(screen)
    else:
        group.empty()


'''
x = 600
y = 360
width = 60
height = 60
vel = 14


def main():
    pygame.init()
    clock = pygame.time.Clock()

    fps = 50
    bg = [0, 0, 0]


    player = Sprite([40, 50])
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    player.vx = 5
    player.vy = 5


    mob = npc([200, 60])

    player_group = pygame.sprite.Group()
    player_group.add(player)

    mob_group = pygame.sprite.Group()
    mob_group.add(mob)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        key = pygame.key.get_pressed()

        for i in range(2):
            if key[player.move[i]]:
                player.rect.x += player.vx * [-1, 1][i]

        for i in range(2):
            if key[player.move[2:4][i]]:
                player.rect.y += player.vy * [-1, 1][i]

        screen.fill(bg)
        mob_group.draw(screen)
        player_group.draw(screen)

        # first parameter takes a single sprite
        # second parameter takes sprite groups
        # third parameter is a do kill command if true
        # all group objects colliding with the first parameter object will be
        # destroyed. The first parameter could be bullets and the second one
        # targets although the bullet is not destroyed but can be done with
        # simple trick bellow
        hit = pygame.sprite.spritecollide(player, mob_group, False)
        keys = pygame.key.get_pressed()


        if hit and keys[pygame.K_SPACE]:
            dialogue()



        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit


if __name__ == '__main__':
    main()
'''
