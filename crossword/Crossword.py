from pygame.locals import *
import pygame, sys, eztext



pygame.init()
screen = pygame.display.set_mode((600,800))
font = pygame.font.SysFont("Arial", 50)
title = font.render("Crossword", True, (0, 0, 0))
KEY_REPEAT_SETTING = (200,70)
clock = pygame.time.Clock()
grey = (211,211,211)
clickedgrey = (169,169,169)



font2 = pygame.font.SysFont("Arial", 12)


def textandrectangle(rx,ry,txtbxnum):
        events = pygame.event.get()
        rectanglebox =  pygame.draw.rect(screen,grey, (rx, ry, 10, 10))
        txtbxnum.draw(screen)
        for event in events:
            Update = txtbxnum.update(events)
            if event.type == pygame.MOUSEBUTTONUP:
                px, py = pygame.mouse.get_pos()
                if rectanglebox.collidepoint(px, py):
                    txtbxnum.color = (255,0,0)
                    pygame.draw.rect(screen,clickedgrey, (rx, ry, 10, 10))
                    Update
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                txtbxnum.color = (0,0,0)
            break
            
def Board():
    done = False
    #Across1 (Ron)
    txtbx1 = eztext.Input(maxlength=1, color=(0,0,0), prompt='1 & 4: ', x=281,
                            y = 120)
    txtbx2 = eztext.Input(maxlength=1, color=(0,0,0), prompt='', x=324,
                            y = 120)
    txtbx3 = eztext.Input(maxlength=1, color=(0,0,0), prompt='', x=336,
                            y = 120)

        #Down2 (Seven (n) is in Ron(Across1))

    txtbx4 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=333,
                            y = 72)
    txtbx5 = eztext.Input(maxlength=1, color=(0,0,0), prompt='2: ', x=324,
                            y = 84)
    txtbx6 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=333,
                            y = 96)
    txtbx7 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=333,
                            y = 108)
        #Across3 (MischiefManaged (s) is in Seven(Down2))
    txtbx8 = eztext.Input(maxlength=1, color=(0,0,0), prompt='3: ', x=300,
                        y = 72)
    txtbx9 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=321,
                        y = 72)
    txtbx10 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=333,
                        y = 72)
    txtbx11 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=345,
                        y = 72)
    txtbx12 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=357,
                        y = 72)
    txtbx13 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=369,
                        y = 72)
    txtbx14 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=381,
                        y = 72)
    txtbx15 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=393,
                        y = 72)
    txtbx16 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=405,
                        y = 72)
    txtbx17 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=417,
                    y = 72)
    txtbx18 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=429,
                    y = 72)
    txtbx19 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=441,
                    y = 72)
    txtbx20 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=453,
                    y = 72)
    txtbx21 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=465,
                    y = 72)

    #Down4 (Ravenclaw (r) is in Ron(Across1))
    txtbx22 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=300,
                        y = 120)
    txtbx23 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=300,
                        y = 132)
    txtbx24 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=300,
                        y = 144)
    txtbx25 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=300,
                        y = 156)
    txtbx26 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=300,
                        y = 168)
    txtbx27 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=300,
                        y = 180)
    txtbx28 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=300,
                        y = 192)
    txtbx29 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=300,
                        y = 204)


    #Across5(DeathlyHallows (w) is in Ravenclaw(Down4))
    txtbx30 = eztext.Input(maxlength=1, color=(0,0,0), prompt='5: ', x=144,
                        y = 204)
    txtbx31 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=156,
                    y = 204)
    txtbx32 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=168,
                        y = 204)
    txtbx33 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=180,
                        y = 204)
    txtbx34 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=192,
                        y = 204)
    txtbx35 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=204,
                        y = 204)
    txtbx36 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=216,
                        y = 204)
    txtbx37 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=228,
                        y = 204)
    txtbx38 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=240,
                        y = 204)
    txtbx39 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=252,
                        y = 204)
    txtbx40 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=264,
                        y = 204)
    txtbx41 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=276,
                    y = 204)
    txtbx42 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=288,
                        y = 204)

#Down6(Fleur (f) in Mischief(Across3 #14))
    txtbx43 = eztext.Input(maxlength=1, color=(0,0,0), prompt='6: ', x=385,
                    y = 84)
    txtbx44 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=394,
                        y = 96)
    txtbx45 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=394,
                    y = 108)
    txtbx46 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=394,
                        y = 120)

#Across7(Nagini (n) in Ravenclaw(Down4 #25))
    txtbx47 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=322,
                    y = 168)
    txtbx48 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=334,
                        y = 168)
    txtbx49 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=346,
                    y = 168)
    txtbx50 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=358,
                        y = 168)
    txtbx51 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=370,
                        y = 168)
#Down8(Diadem (d) in Managed(Across3 #21))
    txtbx52 = eztext.Input(maxlength=1, color=(0,0,0), prompt='8: ', x=456,
                    y = 83)
    txtbx53 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=465,
                        y = 95)
    txtbx54 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=465,
                    y = 107)
    txtbx55 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=465,
                        y = 119)
    txtbx56 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=465,
                        y = 131)
#Across9(Percy (e) in Fleur(Down6 #44))
    txtbx57 = eztext.Input(maxlength=1, color=(0,0,0), prompt='9: ', x=373,
                    y = 96)
    txtbx58 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=406,
                        y = 96)
    txtbx59 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=418,
                    y = 96)
    txtbx60 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=430,
                        y = 96)
#Down10(DracoMalfoy (y) is in Deathly(Across5 #36))
    txtbx61 = eztext.Input(maxlength=1, color=(0,0,0), prompt='10: ', x=210,
                    y = 83)
    txtbx62 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=227,
                        y = 95)
    txtbx63 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=227,
                        y = 107)
    txtbx64 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=227,
                        y = 119)
    txtbx65 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=227,
                        y = 131)
    txtbx66 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=227,
                        y = 143)
    txtbx67 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=227,
                        y = 155)
    txtbx68 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=227,
                        y = 167)
    txtbx69 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=227,
                        y = 179)
    txtbx70 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=227,
                        y = 191)

    
    while not done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
                pygame.quit
                sys.exit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
        screen.fill((255,255,255))
        screen.blit(title,
            (300 - title.get_width() // 2, 25 - title.get_height() // 2))

        Across = font.render("ACROSS:", True, (0,0,0))
        screen.blit(Across,
            (125 - Across.get_width() // 2, 350 - Across.get_height() // 2))

        Down = font.render("DOWN:", True, (0,0,0))
        screen.blit(Down,
            (95 - Down.get_width() // 2, 510 - Down.get_height() // 2))


        Question1 = font2.render("1. The only Weasley that didnt fight for the Order at the Battle of Hogwarts", True, (0, 0, 0))
        screen.blit(Question1,
            (200 - Question1.get_width() // 2, 400 - Question1.get_height() // 2))

        Question2 = font2.render("2.Tri Wizard Tournament contest that married Bill Weasley", True, (0, 0, 0))
        screen.blit(Question2,
            (158 - Question2.get_width() // 2, 550 - Question2.get_height() // 2))

        Question3 = font2.render("3. To close the Mauraders Map you say:", True, (0, 0, 0))
        screen.blit(Question3,
            (110 - Question3.get_width() // 2, 415 - Question3.get_height() // 2))

        Question4 = font2.render("4. How many Horcrux's did Voldemort create (including Harry)", True, (0, 0, 0))
        screen.blit(Question4,
            (170 - Question4.get_width() // 2, 565 - Question4.get_height() // 2))

        Question5 = font2.render("5. The first friend Harry makes at Hogwarts", True, (0, 0, 0))
        screen.blit(Question5,
            (118 - Question5.get_width() // 2, 430 - Question5.get_height() // 2))

        Question6 = font2.render("6. Hogwarts house containing the colors Blue and Silver", True, (0, 0, 0))
        screen.blit(Question6,
            (155 - Question6.get_width() // 2, 580 - Question6.get_height() // 2))

        Question7 = font2.render("7. The horcrux destroyed by Neville", True, (0, 0, 0))
        screen.blit(Question7,
            (99 - Question7.get_width() // 2, 445 - Question7.get_height() // 2))

        Question8 = font2.render("8. Horcrux tied to Rowena Ravenclaw", True, (0, 0, 0))
        screen.blit(Question8,
            (105 - Question8.get_width() // 2, 595 - Question8.get_height() // 2))

        Question9 = font2.render("9. What does the Invisiblity cloak, Elder wand and Resurection stone combined make?", True, (0, 0, 0))
        screen.blit(Question9,
            (236 - Question9.get_width() // 2, 460 - Question9.get_height() // 2))

        Question10 = font2.render("10. Who was chosen by Voldemort to kill Dumbledor", True, (0, 0, 0))
        screen.blit(Question10,
            (145 - Question10.get_width() // 2, 610 - Question10.get_height() // 2))



      
#Across1
        #txtbx1
        rectanglebox =  pygame.draw.rect(screen,grey, (311, 120, 10, 10))
        txtbx1.draw(screen)
        for event in events:
            Update1 = txtbx1.update(events)
            if event.type == pygame.MOUSEBUTTONUP:
                px, py = pygame.mouse.get_pos()
                if rectanglebox.collidepoint(px, py):
                    txtbx1.color = (255,0,0)
                    pygame.draw.rect(screen,clickedgrey, (311, 120, 10, 10))
                    Update1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                txtbx1.color = (0,0,0)
            break
            
 
        textandrectangle(323,120,txtbx2)
        textandrectangle(335,120,txtbx3)

#Down2
        textandrectangle(335,72,txtbx4)
        textandrectangle(335,84,txtbx5)
        textandrectangle(335,96,txtbx6)
        textandrectangle(335,108,txtbx7)

#Across3
        textandrectangle(311,72,txtbx8)
        textandrectangle(323,72,txtbx9)
        textandrectangle(347,72,txtbx10)
        textandrectangle(359,72,txtbx11)
        textandrectangle(371,72,txtbx12)
        textandrectangle(383,72,txtbx13)
        textandrectangle(395,72,txtbx14)
        textandrectangle(407,72,txtbx15)
        textandrectangle(419,72,txtbx16)
        textandrectangle(431,72,txtbx17)
        textandrectangle(443,72,txtbx18)
        textandrectangle(455,72,txtbx19)
        textandrectangle(467,72,txtbx20)
        textandrectangle(479,72,txtbx21)
                
#Down4
        textandrectangle(311,132,txtbx22)
        textandrectangle(311,144,txtbx23)
        textandrectangle(311,156,txtbx24)
        textandrectangle(311,168,txtbx25)
        textandrectangle(311,180,txtbx26)
        textandrectangle(311,192,txtbx27)
        textandrectangle(311,204,txtbx28)
        textandrectangle(311,216,txtbx29)

#Across5
        textandrectangle(155,204,txtbx30)
        textandrectangle(167,204,txtbx31)
        textandrectangle(179,204,txtbx32)
        textandrectangle(191,204,txtbx33)
        textandrectangle(203,204,txtbx34)
        textandrectangle(215,204,txtbx35)
        textandrectangle(227,204,txtbx36)
        textandrectangle(239,204,txtbx37)
        textandrectangle(251,204,txtbx38)
        textandrectangle(263,204,txtbx39)
        textandrectangle(275,204,txtbx40)
        textandrectangle(287,204,txtbx41)
        textandrectangle(299,204,txtbx42)
    
#Down6
        textandrectangle(395,84,txtbx43)
        textandrectangle(395,96,txtbx44)
        textandrectangle(395,108,txtbx45)
        textandrectangle(395,120,txtbx46)

#Across7
        textandrectangle(323,168,txtbx47)
        textandrectangle(335,168,txtbx48)
        textandrectangle(347,168,txtbx49)
        textandrectangle(359,168,txtbx50)
        textandrectangle(371,168,txtbx51)
        
#Down8
        textandrectangle(467,84,txtbx52)
        textandrectangle(467,96,txtbx53)
        textandrectangle(467,108,txtbx54)
        textandrectangle(467,120,txtbx55)
        textandrectangle(467,132,txtbx56)

#Across9
        textandrectangle(383,96,txtbx57)
        textandrectangle(407,96,txtbx58)
        textandrectangle(419,96,txtbx59)
        textandrectangle(431,96,txtbx60)
#Down10
        textandrectangle(227,84,txtbx61)
        textandrectangle(227,96,txtbx62)
        textandrectangle(227,108,txtbx63)
        textandrectangle(227,120,txtbx64)
        textandrectangle(227,132,txtbx65)
        textandrectangle(227,144,txtbx66)
        textandrectangle(227,156,txtbx67)
        textandrectangle(227,168,txtbx68)
        textandrectangle(227,180,txtbx69)
        textandrectangle(227,192,txtbx70)

        pygame.display.flip()
        clock.tick(30)
    pygame.display.quit


if __name__ == '__main__': Board()


