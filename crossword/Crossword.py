from pygame.locals import *
import pygame, sys, eztext

## extext borrowed from https://www.pygame.org/project-EzText-920-.html


pygame.init()
screen = pygame.display.set_mode((600,800))
font = pygame.font.SysFont("Arial", 50)
title = font.render("Crossword", True, (0, 0, 0))
KEY_REPEAT_SETTING = (200,70)
clock = pygame.time.Clock()
grey = (211,211,211)
clickedgrey = (169,169,169)
font2 = pygame.font.SysFont("Arial", 12)
currentbox = 1


def textandrectangle(rx,ry,txtbxnum, events,correctaswr):
        global currentbox 
        rectanglebox =  pygame.draw.rect(screen,grey, (rx, ry, 10, 10))
        txtbxnum.draw(screen)
        for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                        px, py = pygame.mouse.get_pos()
                        if rectanglebox.collidepoint(px, py):
                                txtbxnum.color = (255,0,0)
                                pygame.draw.rect(screen,clickedgrey, (rx, ry, 10, 10))
                                currentbox = txtbxnum
                                if txtbxnum.correctans == txtbxnum.restricted:
                                        txtbxnum.color = (0,255,0)
                                                
        if currentbox == txtbxnum:
                currentbox.update(events)
        

def Board():
        
        #Across1 (Ron)
        txtbx1 = eztext.Input(maxlength=1, color=(0,0,0), prompt='1 & 4: ', restricted = 'r', correctans = 'r' ,x=281, y = 120)
        txtbx2 = eztext.Input(maxlength=1, color=(0,0,0), prompt='', x=324, y = 120)
        txtbx3 = eztext.Input(maxlength=1, color=(0,0,0), prompt='', x=336, y = 120)
        #Down2 (Seven (n) is in Ron(Across1))
        txtbx4 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=333, y = 72)
        txtbx5 = eztext.Input(maxlength=1, color=(0,0,0), prompt='2: ', x=324, y = 84)
        txtbx6 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=333, y = 96)
        txtbx7 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=333, y = 108)
        #Across3 (MischiefManaged (s) is in Seven(Down2))
        txtbx8 = eztext.Input(maxlength=1, color=(0,0,0), prompt='3: ', x=300, y = 72)
        txtbx9 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=321, y = 72)
        txtbx10 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=345, y = 72)
        txtbx11 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=357, y = 72)
        txtbx12 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=369, y = 72)
        txtbx13 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=381, y = 72)
        txtbx14 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=393, y = 72)
        txtbx15 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=405, y = 72)
        txtbx16 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=417, y = 72)
        txtbx17 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=429, y = 72)
        txtbx18 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=441, y = 72)
        txtbx19 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=453, y = 72)
        txtbx20 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=465, y = 72)
        txtbx21 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=477, y = 72)
        #Down4 (Ravenclaw (r) is in Ron(Across1))
        txtbx22 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=309, y = 132)
        txtbx23 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=309, y = 144)
        txtbx24 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=309, y = 156)
        txtbx25 = eztext.Input(maxlength=1, color=(0,0,0), prompt='4: ', x=300, y = 168)
        txtbx26 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=309, y = 180)
        txtbx27 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=309, y = 192)
        txtbx28 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=309, y = 204)
        txtbx29 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=309, y = 216)
        #Across5(DeathlyHallows (w) is in Ravenclaw(Down4))
        txtbx30 = eztext.Input(maxlength=1, color=(0,0,0), prompt='5: ', x=155, y = 216)
        txtbx31 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=177, y = 216)
        txtbx32 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=189, y = 216)
        txtbx33 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=201, y = 216)
        txtbx34 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=213, y = 216)
        txtbx35 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=225, y = 216)
        txtbx36 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=237, y = 216)
        txtbx37 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=249, y = 216)
        txtbx38 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=261, y = 216)
        txtbx39 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=273, y = 216)
        txtbx40 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=285, y = 216)
        txtbx41 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=297, y = 216)
        txtbx42 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=321, y = 216)
        #Down6(Fleur (f) in Mischief(Across3 #14))
        txtbx43 = eztext.Input(maxlength=1, color=(0,0,0), prompt='6: ', x=385, y = 84)
        txtbx44 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=394, y = 96)
        txtbx45 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=394, y = 108)
        txtbx46 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=394, y = 120)
        #Across7(Nagini (n) in Ravenclaw(Down4 #25))
        txtbx47 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=322, y = 168)
        txtbx48 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=334, y = 168)
        txtbx49 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=346, y = 168)
        txtbx50 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=358, y = 168)
        txtbx51 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=370, y = 168)
        #Down8(Diadem (d) in Managed(Across3 #21))
        txtbx52 = eztext.Input(maxlength=1, color=(0,0,0), prompt='8: ', x=456, y = 83)
        txtbx53 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=465, y = 95)
        txtbx54 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=465, y = 107)
        txtbx55 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=465, y = 119)
        txtbx56 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=465, y = 131)
        #Across9(Percy (e) in Fleur(Down6 #44))
        txtbx57 = eztext.Input(maxlength=1, color=(0,0,0), prompt='9: ', x=373, y = 96)
        txtbx58 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=406, y = 96)
        txtbx59 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=418, y = 96)
        txtbx60 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=430, y = 96)
        #Down10(DracoMalfoy (y) is in Deathly(Across5 #36))
        txtbx61 = eztext.Input(maxlength=1, color=(0,0,0), prompt='10: ', x=211, y = 96)
        txtbx62 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=226, y = 108)
        txtbx63 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=226, y = 120)
        txtbx64 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=226, y = 132)
        txtbx65 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=226, y = 144)
        txtbx66 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=226, y = 156)
        txtbx67 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=226, y = 168)
        txtbx68 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=226, y = 180)
        txtbx69 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=226, y = 192)
        txtbx70 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', x=226, y = 204)

        correct1 = "r"
        correct2 = "o"
        correct3 = "n"

        correct4 = "S"
        correct5 = "e"
        correct6 = "v"
        correct7 = "e"
        
        correct8 = "M"
        correct9 = "i"
        correct10 = "c"
        correct11 = "h"       
        correct12 = "i"
        correct13 = "e"
        correct14 = "f"
        correct15 = "M"
        correct16 = "a"
        correct17 = "n"
        correct18 = "a"
        correct19 = "g"
        correct20 = "e"
        correct21 = "d"
        
        correct22 = "a"
        correct23 = "v"
        correct24 = "e"
        correct25 = "n"
        correct26 = "c"
        correct27 = "l"
        correct28 = "a"
        correct29 = "w"
        
        correct30 = "D"
        correct31 = "e"
        correct32 = "a"
        correct33 = "t"
        correct34 = "h"
        correct35 = "l"
        correct36 = "y"
        correct37 = "H"
        correct38 = "a"
        correct39 = "l"
        correct40 = "l"
        correct41 = "o"
        correct42 = "s"
        
        correct43 = "l"
        correct44 = "e"
        correct45 = "u"
        correct46 = "r"
        
        correct47 = "a"
        correct48 = "g"
        correct49 = "i"
        correct50 = "n"
        correct51 = "i"
        
        correct52 = "i"
        correct53 = "a"
        correct54 = "d"
        correct55 = "e"
        correct56 = "m"
        
        correct57 = "P"
        correct58 = "r"
        correct59 = "c"
        correct60 = "y"
        
        correct61 = "D"
        correct62 = "r"
        correct63 = "a"
        correct64 = "c"
        correct65 = "o"
        correct66 = "M"
        correct67 = "a"
        correct68 = "l"
        correct69 = "f"
        correct70 = "o"

  

        done = False
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

                screen.blit(title,(300 - title.get_width() // 2, 25 - title.get_height() // 2))

                Across = font.render("ACROSS:", True, (0,0,0))
                screen.blit(Across,(125 - Across.get_width() // 2, 350 - Across.get_height() // 2))

                Down = font.render("DOWN:", True, (0,0,0))
                screen.blit(Down,(95 - Down.get_width() // 2, 510 - Down.get_height() // 2))

                Question1 = font2.render("1. The only Weasley that didnt fight for the Order at the Battle of Hogwarts", True, (0, 0, 0))
                screen.blit(Question1,(200 - Question1.get_width() // 2, 400 - Question1.get_height() // 2))

                Question2 = font2.render("2.Tri Wizard Tournament contest that married Bill Weasley", True, (0, 0, 0))
                screen.blit(Question2,(158 - Question2.get_width() // 2, 550 - Question2.get_height() // 2))

                Question3 = font2.render("3. To close the Mauraders Map you say:", True, (0, 0, 0))
                screen.blit(Question3,(110 - Question3.get_width() // 2, 415 - Question3.get_height() // 2))

                Question4 = font2.render("4. How many Horcrux's did Voldemort create (including Harry)", True, (0, 0, 0))
                screen.blit(Question4,(170 - Question4.get_width() // 2, 565 - Question4.get_height() // 2))

                Question5 = font2.render("5. The first friend Harry makes at Hogwarts", True, (0, 0, 0))
                screen.blit(Question5,(118 - Question5.get_width() // 2, 430 - Question5.get_height() // 2))

                Question6 = font2.render("6. Hogwarts house containing the colors Blue and Silver", True, (0, 0, 0))
                screen.blit(Question6,(155 - Question6.get_width() // 2, 580 - Question6.get_height() // 2))

                Question7 = font2.render("7. The horcrux destroyed by Neville", True, (0, 0, 0))
                screen.blit(Question7,(99 - Question7.get_width() // 2, 445 - Question7.get_height() // 2))

                Question8 = font2.render("8. Horcrux tied to Rowena Ravenclaw", True, (0, 0, 0))
                screen.blit(Question8,(105 - Question8.get_width() // 2, 595 - Question8.get_height() // 2))

                Question9 = font2.render("9. What does the Invisiblity cloak, Elder wand and Resurection stone combined make?", True, (0, 0, 0))
                screen.blit(Question9,(236 - Question9.get_width() // 2, 460 - Question9.get_height() // 2))

                Question10 = font2.render("10. Who was chosen by Voldemort to kill Dumbledore", True, (0, 0, 0))
                screen.blit(Question10,(145 - Question10.get_width() // 2, 610 - Question10.get_height() // 2))


                #Across1
                textandrectangle(311,120,txtbx1,events,correct1)
                textandrectangle(323,120,txtbx2,events,correct2)
                textandrectangle(335,120,txtbx3,events,correct3)
                #Down2
                textandrectangle(335,72,txtbx4,events,correct4)
                textandrectangle(335,84,txtbx5,events,correct5)
                textandrectangle(335,96,txtbx6,events,correct6)
                textandrectangle(335,108,txtbx7,events,correct7)

                #Across3
                textandrectangle(311,72,txtbx8,events,correct8)
                textandrectangle(323,72,txtbx9,events,correct9)
                textandrectangle(347,72,txtbx10,events,correct10)
                textandrectangle(359,72,txtbx11,events,correct11)
                textandrectangle(371,72,txtbx12,events,correct12)
                textandrectangle(383,72,txtbx13,events,correct13)
                textandrectangle(395,72,txtbx14,events,correct14)
                textandrectangle(407,72,txtbx15,events,correct15)
                textandrectangle(419,72,txtbx16,events,correct16)
                textandrectangle(431,72,txtbx17,events,correct17)
                textandrectangle(443,72,txtbx18,events,correct18)
                textandrectangle(455,72,txtbx19,events,correct19)
                textandrectangle(467,72,txtbx20,events,correct20)
                textandrectangle(479,72,txtbx21,events,correct21)

                #Down4
                textandrectangle(311,132,txtbx22,events,correct22)
                textandrectangle(311,144,txtbx23,events,correct23)
                textandrectangle(311,156,txtbx24,events,correct24)
                textandrectangle(311,168,txtbx25,events,correct25)
                textandrectangle(311,180,txtbx26,events,correct26)
                textandrectangle(311,192,txtbx27,events,correct27)
                textandrectangle(311,204,txtbx28,events,correct28)
                textandrectangle(311,216,txtbx29,events,correct29)

                #Across5
                textandrectangle(167,216,txtbx30,events,correct30)
                textandrectangle(179,216,txtbx31,events,correct31)
                textandrectangle(191,216,txtbx32,events,correct32)
                textandrectangle(203,216,txtbx33,events,correct33)
                textandrectangle(215,216,txtbx34,events,correct34)
                textandrectangle(227,216,txtbx35,events,correct35)
                textandrectangle(239,216,txtbx36,events,correct36)
                textandrectangle(251,216,txtbx37,events,correct37)
                textandrectangle(263,216,txtbx38,events,correct38)
                textandrectangle(275,216,txtbx39,events,correct39)
                textandrectangle(287,216,txtbx40,events,correct40)
                textandrectangle(299,216,txtbx41,events,correct41)
                textandrectangle(323,216,txtbx42,events,correct42)

                #Down6
                textandrectangle(395,84,txtbx43,events,correct43)
                textandrectangle(395,96,txtbx44,events,correct44)
                textandrectangle(395,108,txtbx45,events,correct45)
                textandrectangle(395,120,txtbx46,events,correct46)

                #Across7
                textandrectangle(323,168,txtbx47,events,correct47)
                textandrectangle(335,168,txtbx48,events,correct48)
                textandrectangle(347,168,txtbx49,events,correct49)
                textandrectangle(359,168,txtbx50,events,correct50)
                textandrectangle(371,168,txtbx51,events,correct51)

                #Down8
                textandrectangle(467,84,txtbx52,events,correct52)
                textandrectangle(467,96,txtbx53,events,correct53)
                textandrectangle(467,108,txtbx54,events,correct54)
                textandrectangle(467,120,txtbx55,events,correct55)
                textandrectangle(467,132,txtbx56,events,correct56)

                #Across9
                textandrectangle(383,96,txtbx57,events,correct57)
                textandrectangle(407,96,txtbx58,events,correct58)
                textandrectangle(419,96,txtbx59,events,correct59)
                textandrectangle(431,96,txtbx60,events,correct60)

                #Down10
                textandrectangle(227,96,txtbx61,events,correct61)
                textandrectangle(227,108,txtbx62,events,correct62)
                textandrectangle(227,120,txtbx63,events,correct63)
                textandrectangle(227,132,txtbx64,events,correct64)
                textandrectangle(227,144,txtbx65,events,correct65)
                textandrectangle(227,156,txtbx66,events,correct66)
                textandrectangle(227,168,txtbx67,events,correct67)
                textandrectangle(227,180,txtbx68,events,correct68)
                textandrectangle(227,192,txtbx69,events,correct69)
                textandrectangle(227,204,txtbx70,events,correct70)

                pygame.display.flip()
                clock.tick(30)
        pygame.display.quit


if __name__ == '__main__':Board()
