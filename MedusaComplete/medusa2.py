import hitbox
import pickle
import pygame, sys
from pygame.locals import *
pygame.init()


#win.blit(map,(0 -CameraX,0 -CameraY))
#pygame.display.flip()
def main_game():
    pygame.display.set_caption("First Game")

    x = 220
    y = 360
    width = 53
    height = 77
    vel = 30

    forest = False
    room = True
    cave = False
    town = False
    rocks = False
    appleininv = False
    journalininv = False
    journalquest = False
    medusamission = False
    end = False
    introdone = False

    walkLeft = ["l1.png", "l2.png", "l3.png", "l2.png"]

    walkRight = ['r1.png', 'r2.png', 'r3.png', "r2.png"]

    walkUp = ['b1.png', 'b2.png', 'b3.png', 'b2.png']

    walkDown = ['f1.png', 'f2.png', 'f3.png', 'f2.png']

    class Circle(pygame.sprite.Sprite):

        def __init__(self, pos_x, pos_y,win, pic):
            super().__init__()
            self.win = win
            self.open_close = 1
            self.image = pygame.image.load(pic).convert()
            self.image = pygame.transform.scale(self.image, (50,50))
            self.rect = win.blit( self.image, ( pos_x,pos_y))
            self.pos_y = pos_y
            self.pos_x = pos_x
            self.speed_y = 0

        def update(self, GRAVITY, posy,open_close):
            if open_close == 1:
                self.speed_y += GRAVITY
                self.pos_y += self.speed_y
                self.rect.y = self.pos_y
                if self.pos_y > self.win.get_height()-posy-50:
                    self.speed_y = -1
            elif open_close == 2:
                self.speed_y += GRAVITY
                self.pos_y -= self.speed_y
                self.rect.y = self.pos_y

                if self.pos_y < self.win.get_height()-400:
                    self.pos_y = 50
                    self.speed_y = 0




    questbegin = False
    journalquest = False

    introtext = [ "Use your mouse to click through text.", "Use WASD or arrow keys to move.", " Use 'i' or 'e' to check your inventory.", "Press space to interact with villagers and objects.", "Tired of the hustle and bustle of city life...","...you have just moved to a small village.", "Now leave the house and talk to the villagers!", "Maybe you’ll discover something along the way…"]
    Atext = ["Hey did you hear they stopped making socks?", "Crazy stuff right?", "Kinda weird they stopped now, I mean...", "...socks were so popular!", "Oh yea also there's a monster in the woods.", "But I mean, socks! What's up with that?", "this isn't meant to be shown"]
    Mtext = ["You don't look like you're from around here...", "...my name is Mimi!", "My sister bakes the most wonderful macarons...", "...but they're not for you! Hahaha!", "They say there's creatures in those woods.", "Normally I wouldn't care...", "...but one time a girl went in and never came back.", "this isn't meant to be shown"]
    Ktext1 = ["Duuuuuuuuuuuuuuuuuuude!", "I heard there’s some sick fruit in the woods.", "Would you, like, mind grabbing me an apple?", "It’ll go great with my Monster energy drink!", "The doorway to the right is the entrance of the forest.", "There's a little tree on the border of the forest.", "You'll find apples there.", "this isn't meant to be shown"]
    Ktext2 = ["Please grab me an apple from the woods.", "The doorway to the right is the entrance of the forest.", "There's a little tree on the border of the forest.", "You'll find apples there.", "this isn't meant to be shown"]
    Ktext3 = ["YOOOOOOOOOOOOOOOOOOOOOOO!", "BROSKI! THANKS A BUNCH!", "My good friend got lost in those woods some years back", "They say nothing was left of her...", "...but I'm not totally convinced.", "If you were to find her diary out in the woods...", "...that might give you some clues about where she is.", "She had a weird fascination with rocks...", "...try checking under the rocks in the forest, bro.", "Now if you’ll excuse me, I have some drywall to punch.", "this isn't meant to be shown"]
    Ktext4 = ["I really hope you can find my friend...", "this isn't meant to be shown"]
    Ktext5 = ["Wait, so she's alive? And she's the monster?","Oh no...I cast out my main broski!", "This has to be fixed like, right now.", "this isn't meant to be shown"]
    Rtextwrong = ["You look under the rock.", "There is nothing underneath.", "this isn't meant to be shown"]
    Rtextright= ["Score! You found the apple.", "Bring the apple back to Kyle!", "this isn't meant to be shown"]
    Treedefault = ["Just a normal apple tree.", "this isn't meant to be shown"]
    Medtext1 = ["Oh, a visitor… I don’t get many of those nowadays… ", "I wasn’t always like this, you know.", "I used to live in the village with the others.", "One day I wandered into the woods and a witch cursed me.", "Everytime I go into the village they get scared.", "I miss my mom.", "I need you to help me.", "Oh, you found my journal! Haven't seen that in ages.", "Give it to my friend Kyle for me.", "this isn't meant to be shown"]
    Robtainjournal = ["You found the journal! Let's read what's inside...", "'July 21st, 201X.'", "'I've been lost in this cave for months.'", "'I'm scared, I hope someone finds me...'", "'The villagers think that I’m a monster...'", "'Go to the cave and talk to Medusa.'", "this isn't meant to be shown"]
    Rnotjournaltime = ["It's someone's old journal.", "Best to leave it in case they come looking for it.", "this isn't meant to be shown"]
    theend = ["You saved the town and Medusa! Good job!", "The end!", "this isn't meant to be shown"]


    player = pygame.sprite.Group(hitbox.Sprite([200, 200], "f2.png"))
    mob = hitbox.npc([845, 632], "mimi.png")
    mob_group = pygame.sprite.Group()
    mob_group.add(mob)

    aziz_group = pygame.sprite.Group()
    kyle_group = pygame.sprite.Group()
    rock1_group = pygame.sprite.Group()
    rock2_group = pygame.sprite.Group()
    rock3_group = pygame.sprite.Group()
    tree_group = pygame.sprite.Group()
    medusa_group = pygame.sprite.Group()

    character="f2.png"
    #player = pygame.image.load(character).convert_alpha()
    #player = pygame.transform.scale(player, (53,77))

    mapy = pygame.image.load("bedroom.png")
    mapy = pygame.transform.scale(mapy, (1200,950))
    pygame.mixer.music.load("house.mp3")
    pygame.mixer.music.play(-1,0.0)
    pygame.display.update()


    CameraX = 30
    CameraY = 160

    counter = 0

    run = True

    boundary_x_lower = 0
    boundary_x_upper = 500

    clock = pygame.time.Clock()
    counter = 0
    run = True
    fps = 120
    #win.blit(mapy,(0 -CameraX,0 -CameraY))
    #pygame.display.flip()


    #iv = pygame.sprite.Group(Circle(400,50, win,"sword.jpg"))
    win = pygame.display.set_mode((500,500))
    iv2 = pygame.sprite.Group(Circle(400,50, win,"empty.png"))
    iv3 = pygame.sprite.Group(Circle(400, 50, win,"journal.png"))
    iv4 = pygame.sprite.Group(Circle(400,50, win,"apple.png"))
    iv5 = pygame.sprite.Group(Circle(400,50, win, "backpack.png"))
    open_iv = False
    closed_iv = False

    while run:
        iv5.draw(win)
        pygame.display.update()
        pygame.time.delay(20)

        event = pygame.event.get()

        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        #hit = pygame.sprite.groupcollide(player, mob_group, False, False)
        win.blit(mapy,(0 -CameraX,0 -CameraY))
        #mob_group.draw(mapy)
        if keys[pygame.K_h]:
            print(x, y)
        player.draw(win)
        iv5.draw(win)
        if x==220 and y == 360 and room == True and questbegin == False and introdone == False:
            #win.blit(mapy,(0 -CameraX,0 -CameraY))
            hitbox.dialogue(introtext, "")
            introdone = True

        def redrawChar(x,y, pic):
            player.empty()
            player.add(hitbox.Sprite([x, y], pic))
            player.draw(win)
            pygame.display.flip()


        if keys[pygame.K_SPACE] and x>=800 and x<=880 and y >= 580 and y <= 660 and town == True:
            #win.blit(mapy,(0 -CameraX,0 -CameraY))
            hitbox.dialogue(Mtext, "Mimi")
        if keys[pygame.K_SPACE] and x>=90 and x<=150 and y >= 748 and y <= 828 and town == True:
            #win.blit(mapy,(0 -CameraX,0 -CameraY))
            hitbox.dialogue(Atext, "Aziz")
        if keys[pygame.K_SPACE] and x>=623 and x<=703 and y >= 146 and y <= 246 and questbegin == False and town == True:
            #win.blit(mapy,(0 -CameraX,0 -CameraY))
            hitbox.dialogue(Ktext1, "Kyle")
            questbegin = True
        elif keys[pygame.K_SPACE] and x>=623 and x<=703 and y >= 146 and y <= 246 and questbegin == True and town == True and appleininv == False and journalquest == False:
            hitbox.dialogue(Ktext2, "Kyle")
        if keys[pygame.K_SPACE] and x>=623 and x<=703 and y >= 298 and y <= 388 and questbegin == True and rocks == True:
            #win.blit(mapy,(0 -CameraX,0 -CameraY))
            hitbox.dialogue(Rtextwrong, "")
        if keys[pygame.K_SPACE] and x>=823 and x<=903 and y >= 498 and y <= 588 and questbegin == True and rocks == True:
            #win.blit(mapy,(0 -CameraX,0 -CameraY))
            hitbox.dialogue(Rtextwrong, "")
        if keys[pygame.K_SPACE] and x>=950 and x<=1050 and y >= 425 and y <= 515 and questbegin == True and rocks == True and journalquest == False:
            #win.blit(mapy,(0 -CameraX,0 -CameraY))
            hitbox.dialogue(Rtextright, "")
            appleininv = True
        elif keys[pygame.K_SPACE] and x>=950 and x<=1050 and y >= 425 and y <= 515 and journalquest == True and rocks == True:
            #win.blit(mapy,(0 -CameraX,0 -CameraY))
            hitbox.dialogue(Treedefault, "")
        if keys[pygame.K_SPACE] and x>=623 and x<=703 and y >= 146 and y <= 246 and questbegin == True and town == True and appleininv == True:
            hitbox.dialogue(Ktext3, "Kyle")
            appleininv = False
            journalquest = True
        elif keys[pygame.K_SPACE] and x>=623 and x<=703 and y >= 146 and y <= 246 and questbegin == True and town == True and appleininv == False and journalquest == True and medusamission == False:
            hitbox.dialogue(Ktext4, "Kyle")
        if keys[pygame.K_SPACE] and x>=585 and x<=665 and y >= 610 and y <= 690 and rocks == True and journalquest == True:
            #win.blit(mapy,(0 -CameraX,0 -CameraY))
            hitbox.dialogue(Robtainjournal, "")
            journalininv = True
        elif keys[pygame.K_SPACE] and x>=585 and x<=665 and y >= 610 and y <= 690 and rocks == True and journalquest == False:
            #win.blit(mapy,(0 -CameraX,0 -CameraY))
            hitbox.dialogue(Rnotjournaltime, "")
        if keys[pygame.K_SPACE] and x>=613 and x<=703 and y >= 498 and y <= 588 and cave == True and journalquest == True and journalininv == True:
            hitbox.dialogue(Medtext1, "Medusa")
            medusamission = True
        if keys[pygame.K_SPACE] and x>=623 and x<=703 and y >= 146 and y <= 246 and questbegin == True and town == True and appleininv == False and journalininv == True and medusamission == True:
            hitbox.dialogue(Ktext5, "Kyle")
            room = True
            town = False
            end = True


        if x>=90 and x<=150 and y >= 748 and y <= 828 and town == True:
            azizexclaim = True
            hitbox.check_npc(azizexclaim,130, 788,"azizexclaim.png", mapy, aziz_group)
        elif x>=800 and x<=880 and y >= 580 and y <= 660 and town == True:
            mimiexclaim = True
            hitbox.check_npc(mimiexclaim,845, 632,"mimiexclaim.png", mapy, mob_group)
        elif x>=623 and x<=703 and y >= 146 and y <= 246 and town == True:
            kyleexclaim = True
            hitbox.check_npc(kyleexclaim,663, 196,"kyleexclaim.png", mapy, kyle_group)
        elif  x>=623 and x<=703 and y >= 298 and y <= 388 and rocks == True:
            rock1exclaim = True
            hitbox.check_npc(rock1exclaim,663, 338,"rock1exclaim.png", mapy, rock1_group)
        elif x>=823 and x<=903 and y >= 498 and y <= 588 and rocks == True:
            rock2exclaim = True
            hitbox.check_npc(rock2exclaim,863, 538,"rock1exclaim.png", mapy, rock2_group)
        elif x>=585 and x<=665 and y >= 610 and y <= 690 and rocks == True:
            rock3exclaim = True
            hitbox.check_npc(rock3exclaim,625, 650,"rock1exclaim.png", mapy, rock3_group)
        elif x>=950 and x<=1050 and y >= 425 and y <= 515 and rocks == True:
            treeexclaim = True
            hitbox.check_npc(treeexclaim,1000, 475,"treeexclaim.png", mapy, tree_group)
        elif x>=613 and x<=703 and y >= 498 and y <= 588 and cave == True:
            medusaexclaim = True
            hitbox.check_npc(medusaexclaim,663, 538,"medusaexclaim.png", mapy, medusa_group)

    #    if x>=623 and x<=703 and y >= 146 and y <= 246 and room == True and questbegin == True and town == False and appleininv == False and journalininv == True and medusamission == True and end == True:
    #        end
    #        hitbox.dialogue(theend, "")


        pygame.display.update()
        clock.tick(fps)
        #win.blit(mapy,(0 -CameraX,0 -CameraY))
        #pygame.display.flip()

        clock.tick(fps)


        if keys[pygame.K_LEFT] or keys[pygame.K_a]:

            ###
        #    player.update(walkLeft[counter])

            ##
            counter = (counter + 1) % len(walkLeft)
            old_x = x
            old_y = y
            x -= vel
            CameraX -= 20
            if x <= 20:
                x += 40
    #        if x <= 25:
    #            x += 55
            if CameraX <= 0:
                CameraX += 20
            #win.fill(0,0,0)
            player.empty()
            player.add(hitbox.Sprite([old_x-CameraX, old_y-CameraY], walkLeft[counter]))
            win.fill((0,0,0))
            win.blit(mapy,(0 -CameraX,0 -CameraY))
            #mob_group.draw(mapy)
            player.draw(win)
            iv5.draw(win)
            #player.remove()


            pygame.display.flip()

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:

            ###

            ##


            counter = (counter + 1) % len(walkRight)
            old_x = x
            old_y = y
            x += vel
            CameraX += 20
            if x >= 1060:
                x -= 40
    #        if x >= 1030:
    #            x -= 55
            if CameraX >= 650:
                CameraX -= 20

            player.empty()
            player.add(hitbox.Sprite([old_x-CameraX, old_y-CameraY], walkRight[counter]))
            win.fill((0,0,0))
            win.blit(mapy,(0 -CameraX,0 -CameraY))
            #mob_group.draw(mapy)
            player.draw(win)
            iv5.draw(win)
            #player.remove()

            pygame.display.flip()

        elif keys[pygame.K_UP] or keys[pygame.K_w]:

            ###

            ##

            counter = (counter + 1) % len(walkUp)
            old_x = x
            old_y = y
            y -= vel
            CameraY -= 20

            if y <= 20:
                y += 40
    #        if y <= 15:
    #            y += 55
            if CameraY <= 0:
                CameraY += 20

            player.empty()
            player.add(hitbox.Sprite([old_x-CameraX, old_y-CameraY], walkUp[counter]))
            win.fill((0,0,0))
            win.blit(mapy,(0 -CameraX,0 -CameraY))
            #mob_group.draw(mapy)
            player.draw(win)
            iv5.draw(win)
            #player.remove()

            pygame.display.flip()

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:

            ###

            ##

            counter = (counter + 1) % len(walkDown)
            old_x = x
            old_y = y
            y += vel
            CameraY += 20
            if y >= 900:
                y -= 40
    #            y -= 55

            if CameraY >= 450:
                CameraY -= 20

            player.empty()
            player.add(hitbox.Sprite([old_x-CameraX, old_y-CameraY], walkDown[counter]))
            win.fill((0,0,0))
            win.blit(mapy,(0 -CameraX,0 -CameraY))
            #mob_group.draw(mapy)
            player.draw(win)
            iv5.draw(win)
            #player.remove()

            pygame.display.flip()



        if keys[pygame.K_TAB]:
            for i in range(0,150):
                #iv.update(.1,0,2)
                iv2.update(.4,30,2)
                iv3.update(.4,30,2)
                iv4.update(.4,30,2)
                win.fill((0,0,0))  # Fills the win with black
                win.blit(mapy,(0 -CameraX,0 -CameraY))
                #win.blit(player,(x -CameraX,y -CameraY))
                player.draw(win)
                #iv.draw(win)
                iv2.draw(win)
                iv3.draw(win)
                iv4.draw(win)
                iv5.draw(win)

                pygame.display.update()
                clock.tick(fps)

        if keys[pygame.K_i] or keys[pygame.K_e]:
            for i in range(0,100):
                #iv.update(.1,0,1)
                iv2.update(.4,300,1)
                iv3.update(.4,300,1)
                iv4.update(.4,300,1)
                win.fill((0,0,0))  # Fills the win with black
                win.blit(mapy,(0 -CameraX,0 -CameraY))
                #win.blit(player,(x -CameraX,y -CameraY))
                player.draw(win)
                #iv.draw(win)
                if journalininv == True:
                    iv3.draw(win)
                elif appleininv == True:
                    iv4.draw(win)
                else:
                    iv2.draw(win)
                iv5.draw(win)

                pygame.display.flip()
                clock.tick(fps)

        if end == True:  #town to end
            cave = False
            room = True
            town = False
            forest = False
            rocks = False
            mapy = pygame.image.load("bedroom.png")
#            pygame.mixer.music.load("house.mp3")
#            pygame.mixer.music.play(-1,0.0)


            ###
            player.update(character)
            character = 'f2.png'
            player.draw(win)


            mapy = pygame.transform.scale(mapy, (1200,950))
            x = 250
            y = 360
            CameraX = 30
            CameraY = 160
            hitbox.check_npc(room,150, 360,"mimi.png", mapy, mob_group)
            hitbox.check_npc(room,200, 360,"aziz.png", mapy, aziz_group)
            hitbox.check_npc(room,300, 360,"kyle.png", mapy, kyle_group)
            hitbox.check_npc(room,350, 360,"medusa.png", mapy, medusa_group)


            player.update(character)
            player.draw(win)
            pygame.display.update()
            hitbox.dialogue(theend, "")
            main_menu()



        if forest == False and room == True and cave== False and town == True and end == True:  #town to end
            cave = False
            room = True
            town = False
            forest = False
            rocks = False

            CameraX = 30
            CameraY = 160
            redrawChar(x,y, "f2.png")
            mapy = pygame.image.load("bedroom.png")
            mapy = pygame.transform.scale(mapy, (1200,950))
            pygame.display.update()
            pygame.mixer.music.load("house.mp3")
            pygame.mixer.music.play(-1,0.0)

            ###
            character = 'f2.png'

            hitbox.check_npc(room,150, 360,"mimi.png", mapy, mob_group)
            hitbox.check_npc(room,200, 360,"aziz.png", mapy, aziz_group)
            hitbox.check_npc(room,300, 360,"kyle.png", mapy, kyle_group)
            hitbox.check_npc(room,350, 360,"medusa.png", mapy, medusa_group)

            x = 250
            y = 360
            pygame.display.update()

        if x >=670 and x <= 895 and y >= 870 and forest == False and room == True and cave== False and town == False:  #room start to town
            cave = False
            room = False
            town = True
            forest = False
            rocks = False

            CameraX = 0
            CameraY = 240
            redrawChar(x,y, "f2.png")
            mapy = pygame.image.load("ntown.png")
            mapy = pygame.transform.scale(mapy, (1200,950))
        #    pygame.display.update()
            pygame.mixer.music.load("lofty8bit.mp3")
            pygame.mixer.music.play(-1,0.0)

            hitbox.check_npc(town,845, 632,"mimi.png", mapy, mob_group)
            hitbox.check_npc(town,130, 788,"aziz.png", mapy, aziz_group)
            hitbox.check_npc(town,663, 196,"kyle.png", mapy, kyle_group)
            hitbox.check_npc(rocks,663, 338,"rock1.png", mapy, rock1_group)
            hitbox.check_npc(rocks,863, 538,"rock1.png", mapy, rock2_group)
            hitbox.check_npc(rocks,625, 650,"rock1.png", mapy, rock3_group)
            hitbox.check_npc(rocks,1000, 475,"tree.png", mapy, tree_group)
            hitbox.check_npc(cave,663, 538,"medusa.png", mapy, medusa_group)

            ##
            x = 150
            y = 400

            pygame.display.update()



            ##specify x and y
        if x >= 140 and x <= 160 and y <= 360 and room == False and forest == False and cave == False and town == True: #swith from town to room
            cave = False
            room = True
            forest = False
            town = False
            rocks = False
            x = 775
            y = 840
            CameraX = 550
            CameraY = 450
            redrawChar(x,y, "f2.png")
            #pygame.display.update()
            mapy = pygame.image.load("bedroom.png")
            mapy = pygame.transform.scale(mapy, (1200,950))
            pygame.mixer.music.load("house.mp3")
            pygame.mixer.music.play(-1,0.0)

            hitbox.check_npc(town,845, 632,"mimi.png", mapy, mob_group)
            hitbox.check_npc(town,130, 788,"aziz.png", mapy, aziz_group)
            hitbox.check_npc(town,663, 196,"kyle.png", mapy, kyle_group)
            hitbox.check_npc(rocks,663, 338,"rock1.png", mapy, rock1_group)
            hitbox.check_npc(rocks,863, 538,"rock1.png", mapy, rock2_group)
            hitbox.check_npc(rocks,625, 650,"rock1.png", mapy, rock3_group)
            hitbox.check_npc(rocks,1000, 475,"tree.png", mapy, tree_group)
            hitbox.check_npc(cave,663, 538,"medusa.png", mapy, medusa_group)
            ##


            pygame.display.update()

        if x >= 740 and x <= 760 and y >= 110 and y <= 140 and forest == False and room == False and cave == False and town == True and questbegin == True: #switch from town to forest
            cave = False
            room = False
            town = False
            forest = True
            rocks = True

            CameraX = 0
            CameraY = 0
            redrawChar(x,y, "f2.png")
            mapy = pygame.image.load("nforest.png")
            mapy = pygame.transform.scale(mapy, (1200,950))
            pygame.display.update()
            pygame.mixer.music.load("forest2.mp3")
            pygame.mixer.music.play(-1,0.0)


            hitbox.check_npc(town,845, 632,"mimi.png", mapy, mob_group)
            hitbox.check_npc(town,130, 788,"aziz.png", mapy, aziz_group)
            hitbox.check_npc(town,663, 196,"kyle.png", mapy, kyle_group)
            hitbox.check_npc(rocks,663, 338,"rock1.png", mapy, rock1_group)
            hitbox.check_npc(rocks,863, 538,"rock1.png", mapy, rock2_group)
            hitbox.check_npc(rocks,625, 650,"rock1.png", mapy, rock3_group)
            hitbox.check_npc(rocks,1000, 475,"tree.png", mapy, tree_group)
            hitbox.check_npc(cave,663, 538,"medusa.png", mapy, medusa_group)

            ##
            ##
            x = 100 #starting location after mapy change
            y = 175
            pygame.display.update()

        if x >= 0 and x <= 50 and y >=75  and y <=225 and cave == False and room == False and forest == True and town == False: #switch from forest to town
            cave = False
            forest = False
            room = False
            town = True
            rocks = False
            x = 750
            y = 260
            CameraX = 500
            CameraY = 0
            redrawChar(x,y, "f2.png")
            mapy = pygame.image.load("ntown.png")
            mapy = pygame.transform.scale(mapy, (1200,950))
            pygame.display.update()
            pygame.mixer.music.load("lofty8bit.mp3")
            pygame.mixer.music.play(-1,0.0)

            ###

            hitbox.check_npc(town,845, 632,"mimi.png", mapy, mob_group)
            hitbox.check_npc(town,130, 788,"aziz.png", mapy, aziz_group)
            hitbox.check_npc(town,663, 196,"kyle.png", mapy, kyle_group)
            hitbox.check_npc(rocks,663, 338,"rock1.png", mapy, rock1_group)
            hitbox.check_npc(rocks,863, 538,"rock1.png", mapy, rock2_group)
            hitbox.check_npc(rocks,625, 650,"rock1.png", mapy, rock3_group)
            hitbox.check_npc(rocks,1000, 475,"tree.png", mapy, tree_group)
            hitbox.check_npc(cave,663, 538,"medusa.png", mapy, medusa_group)
            ##
            ##

            pygame.display.update()

        if x >= 550 and x <= 800 and y >= 875 and cave == False and room == False and forest == True and town == False and journalininv == True: #swith from forest to cave
            cave = True
            forest = False
            town = False
            rocks = False
            room = False

            CameraX = 50
            CameraY = 50
            redrawChar(x,y, "f2.png")
            mapy = pygame.image.load("cave.png")
            mapy = pygame.transform.scale(mapy, (1200,950))
            pygame.display.update()
            pygame.mixer.music.load("cave2.mp3")
            pygame.mixer.music.play(-1,0.0)

            ###

            hitbox.check_npc(town,845, 632,"mimi.png", mapy, mob_group)
            hitbox.check_npc(town,130, 788,"aziz.png", mapy, aziz_group)
            hitbox.check_npc(town,663, 196,"kyle.png", mapy, kyle_group)
            hitbox.check_npc(rocks,663, 338,"rock1.png", mapy, rock1_group)
            hitbox.check_npc(rocks,863, 538,"rock1.png", mapy, rock2_group)
            hitbox.check_npc(rocks,625, 650,"rock1.png", mapy, rock3_group)
            hitbox.check_npc(rocks,1000, 475,"tree.png", mapy, tree_group)
            hitbox.check_npc(cave,663, 538,"medusa.png", mapy, medusa_group)
        ##
            x = 220
            y = 250
            pygame.display.update()

        if x >= 200 and x <= 240 and y <= 170 and room == False and forest == False and cave == True and town == False: #swith from cave to forest
            cave = False
            forest = True
            town = False
            rocks = True
            x = 710
            y = 750
            CameraX = 500
            CameraY = 500
            redrawChar(x,y, "f2.png")
            mapy = pygame.image.load("nforest.png")
            mapy = pygame.transform.scale(mapy, (1200,950))
            pygame.display.update()
            pygame.mixer.music.load("forest2.mp3")
            pygame.mixer.music.play(-1,0.0)


            ###

            hitbox.check_npc(town,845, 632,"mimi.png", mapy, mob_group)
            hitbox.check_npc(town,130, 788,"aziz.png", mapy, aziz_group)
            hitbox.check_npc(town,663, 196,"kyle.png", mapy, kyle_group)
            hitbox.check_npc(rocks,663, 338,"rock1.png", mapy, rock1_group)
            hitbox.check_npc(rocks,863, 538,"rock1.png", mapy, rock2_group)
            hitbox.check_npc(rocks,625, 650,"rock1.png", mapy, rock3_group)
            hitbox.check_npc(rocks,1000, 475,"tree.png", mapy, tree_group)
            hitbox.check_npc(cave,663, 538,"medusa.png", mapy, medusa_group)


            pygame.display.update()


def creator(screen):
    pygame.display.set_caption("First Game")

    purple = (224,146,247)
    screen_r = screen.get_rect()
    font = pygame.font.SysFont("Arial", 15)
    clock = pygame.time.Clock()

    purple = (224, 146, 247)
    screen.fill(purple)

    credit_list = ["CREDITS - Medusa"," ","Alex- Thought up the plot, cropped sprites, made bad jokes, added music","Emma- showed minecraft parodies, Dialogue and HitBox Engineer, NPC god", "Rita- Made title screen and setting portals. She draws better than me", "Yewon- Movement God, Camera Cod, kept us on task or whatev", "Special thanks to Mimi and google.com ~ "]

    texts = []
    # we render the text once, since it's easier to work with surfaces
    # also, font rendering is a performance killer
    for i, line in enumerate(credit_list):
        s = font.render(line, 1, (10, 10, 10))
        # we also create a Rect for each Surface.
        # whenever you use rects with surfaces, it may be a good idea to use sprites instead
        # we give each rect the correct starting position
        r = s.get_rect(centerx=screen_r.centerx, y=screen_r.bottom + i * 45)
        texts.append((r, s))

    while True:
        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                return

        screen.fill((255, 255, 255))

        for r, s in texts:
            # now we just move each rect by one pixel each frame
            r.move_ip(0, -1)
            # and drawing is as simple as this
            screen.blit(s, r)

        # if all rects have left the screen, we exit
        if not screen_r.collidelistall([r for (r, _) in texts]):
            return

        # only call this once so the screen does not flicker
        pygame.display.flip()

        # cap framerate at 60 FPS
        clock.tick(50)








def main_menu():
    #pygame.init()
    win_width = 500
    win_height = 500
    win = pygame.display.set_mode((500,500))
    #color n font
    white = (255,255,255)
    black = (0,0,0)
    blue = (224,146,247)
    yellow = (255,255,0)

    font = pygame.font.SysFont(None, 20)
    newFont = pygame.font.SysFont(None, 20)

    #text render
    def text_format():
        newFont= pygame.font.Font(None, 50)
        newText = newFont.render("Welcome to Medusa", 50, yellow)
        return newText
    def text_on(text):
        newFont = pygame.font.Font(None, 30)
        newText = newFont.render(text, 75, white)
        return newText
    def text_off(text):
        newFont = pygame.font.Font(None, 30)
        newText = newFont.render(text, 75, black)
        return newText

#frame rate
    clock = pygame.time.Clock()
    FPS = 90


#main menu
    def main_men_run():
        win = pygame.display.set_mode((500,500))
        menu = True
        selected = 0
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP and selected == 0:
                        selected = 2
                    elif event.key ==pygame.K_UP and selected == 1:
                        selected = 0
                    elif event.key == pygame.K_UP and selected == 2:
                        selected = 1

                    if event.key == pygame.K_DOWN and selected == 0:
                        selected = 1
                    elif event.key == pygame.K_DOWN and selected == 1:
                        selected = 2
                    elif event.key == pygame.K_DOWN and selected == 2:
                        selected = 0

                    if event.key == pygame.K_RETURN:
                        if selected == 0: #start
                            print ("start")
                            main_game()
                        if selected ==1: #exit
                            pygame.quit()
                        if selected == 2: #creator page
                            creator(win)


            #menu UI
            win.fill(blue)
            title = text_format()
            #start
            if selected == 0:
                 start = text_on("Start")
                 start_rect = start.get_rect()
            else:
                start = text_off("Start")
                start_rect = start.get_rect()

                        #quit
            if selected == 1:
                 quit = text_on("Quit")
                 quit_rect = quit.get_rect()
            else:
                quit = text_off("Quit")
                quit_rect = quit.get_rect()

                        #creater 2
            if selected == 2:
                creators = text_on("Creators")
                creator_rect = creators.get_rect()
            else:
                creators = text_off("Creators")
                creator_rect = creators.get_rect()



            title_rect = title.get_rect()
            quit_rect = quit.get_rect()
            creator_rect = creators.get_rect()
            #menu text
            win.blit(title,(win_width/2 - (title_rect[2]/2),80))
            win.blit(start,(win_width/2 - (start_rect[2]/2),300))
            win.blit(quit,(win_width/2 - (quit_rect[2]/2), 360))
            win.blit(creators,(win_width/2 - (creator_rect[2]/2), 410))

            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("First Game")
    main_men_run()

#creator page


    #main game run

    #
    ##player is black box
    #    mob_group.draw(mapy)
    #    player.draw(win)
    #    win.fill((0,0,0))  # Fills the screen with black
        #win.blit(mapy,(0 -CameraX,0 -CameraY))
        #player.draw(win)
        #win.blit(player,(x -CameraX,y -CameraY))
        #pygame.display.flip()




main_menu()
pygame.quit()
