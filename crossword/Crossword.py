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


def textandrectangle(rx,ry,txtbxnum, events):
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
                                        txtbxnum.color = (0,139,69)
                                                
        if currentbox == txtbxnum:
                currentbox.update(events)
        

def Board():
        
        #Across1 (Ron)
        txtbx1 = eztext.Input(maxlength=1, color=(0,0,0), prompt='1 & 4: ', restricted = 'Rr', correctans = 'Rr' ,x=281, y = 120)
        txtbx2 = eztext.Input(maxlength=1, color=(0,0,0), prompt='',restricted = 'Oo', correctans = 'Oo' , x=324, y = 120)
        txtbx3 = eztext.Input(maxlength=1, color=(0,0,0), prompt='',restricted = 'Nn', correctans = 'Nn' , x=336, y = 120)
        #Down2 (Seven (n) is in Ron(Across1))
        txtbx4 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Ss', correctans = 'Ss' , x=333, y = 72)
        txtbx5 = eztext.Input(maxlength=1, color=(0,0,0), prompt='2: ',restricted = 'Ee', correctans = 'Ee' , x=324, y = 84)
        txtbx6 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Vv', correctans = 'Vv' , x=333, y = 96)
        txtbx7 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Ee', correctans = 'Ee' , x=333, y = 108)
        #Across3 (MischiefManaged (s) is in Seven(Down2))
        txtbx8 = eztext.Input(maxlength=1, color=(0,0,0), prompt='3: ',restricted = 'Mm', correctans = 'Mm' , x=300, y = 72)
        txtbx9 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Ii', correctans = 'Ii' ,x=321, y = 72)
        txtbx10 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Cc', correctans = 'Cc' ,x=345, y = 72)
        txtbx11 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Hh', correctans = 'Hh' ,x=357, y = 72)
        txtbx12 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Ii', correctans = 'Ii' ,x=369, y = 72)
        txtbx13 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Ee', correctans = 'Ee' ,x=381, y = 72)
        txtbx14 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Ff', correctans = 'Ff' ,x=393, y = 72)
        txtbx15 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Mm', correctans = 'Mm' ,x=405, y = 72)
        txtbx16 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Aa', correctans = 'Aa' ,x=417, y = 72)
        txtbx17 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Nn', correctans = 'Nn' ,x=429, y = 72)
        txtbx18 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Aa', correctans = 'Aa' ,x=441, y = 72)
        txtbx19 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Gg', correctans = 'Gg' ,x=453, y = 72)
        txtbx20 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Ee', correctans = 'Ee' ,x=465, y = 72)
        txtbx21 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Dd', correctans = 'Dd' ,x=477, y = 72)
        #Down4 (Ravenclaw (r) is in Ron(Across1))
        txtbx22 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Aa', correctans = 'Aa' , x=309, y = 132)
        txtbx23 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Vv', correctans = 'Vv' , x=309, y = 144)
        txtbx24 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Ee', correctans = 'Ee' ,x=309, y = 156)
        txtbx25 = eztext.Input(maxlength=1, color=(0,0,0), prompt='4: ',restricted = 'Nn', correctans = 'Nn' , x=300, y = 168)
        txtbx26 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Cc', correctans = 'Cc' ,x=309, y = 180)
        txtbx27 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Ll', correctans = 'Ll' ,x=309, y = 192)
        txtbx28 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Aa', correctans = 'Aa' ,x=309, y = 204)
        txtbx29 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Ww', correctans = 'Ww' ,x=309, y = 216)
        #Across5(DeathlyHallows (w) is in Ravenclaw(Down4))
        txtbx30 = eztext.Input(maxlength=1, color=(0,0,0), prompt='5: ',restricted = 'Dd', correctans = 'Dd' , x=155, y = 216)
        txtbx31 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Ee', correctans = 'Ee' , x=177, y = 216)
        txtbx32 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Aa', correctans = 'Aa' , x=189, y = 216)
        txtbx33 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Tt', correctans = 'Tt' , x=201, y = 216)
        txtbx34 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Hh', correctans = 'Hh' , x=213, y = 216)
        txtbx35 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Ll', correctans = 'Ll' , x=225, y = 216)
        txtbx36 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Yy', correctans = 'Yy' , x=237, y = 216)
        txtbx37 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Hh', correctans = 'Hh' , x=249, y = 216)
        txtbx38 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Aa', correctans = 'Aa' , x=261, y = 216)
        txtbx39 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Ll', correctans = 'Ll' , x=273, y = 216)
        txtbx40 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Ll', correctans = 'Ll' , x=285, y = 216)
        txtbx41 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Ww', correctans = 'Ww' ,x=297, y = 216)
        txtbx42 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Ss', correctans = 'Ss' , x=321, y = 216)
        #Down6(Fleur (f) in Mischief(Across3 #14))
        txtbx43 = eztext.Input(maxlength=1, color=(0,0,0), prompt='6: ',restricted = 'Ll', correctans = 'Ll' , x=385, y = 84)
        txtbx44 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Ee', correctans = 'Ee' , x=394, y = 96)
        txtbx45 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Uu', correctans = 'Uu' , x=394, y = 108)
        txtbx46 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Rr', correctans = 'Rr' , x=394, y = 120)
        #Across7(Nagini (n) in Ravenclaw(Down4 #25))
        txtbx47 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Aa', correctans = 'Aa' , x=322, y = 168)
        txtbx48 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Gg', correctans = 'Gg' , x=334, y = 168)
        txtbx49 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Ii', correctans = 'Ii' , x=346, y = 168)
        txtbx50 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Nn', correctans = 'Nn' , x=358, y = 168)
        txtbx51 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Ii', correctans = 'Ii' , x=370, y = 168)
        #Down8(Diadem (d) in Managed(Across3 #21))
        txtbx52 = eztext.Input(maxlength=1, color=(0,0,0), prompt='8: ',restricted = 'Ii', correctans = 'Ii' , x=456, y = 83)
        txtbx53 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Aa', correctans = 'Aa' , x=465, y = 95)
        txtbx54 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Dd', correctans = 'Dd' , x=465, y = 107)
        txtbx55 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Ee', correctans = 'Ee' , x=465, y = 119)
        txtbx56 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Mm', correctans = 'Mm' , x=465, y = 131)
        #Across9(Percy (e) in Fleur(Down6 #44))
        txtbx57 = eztext.Input(maxlength=1, color=(0,0,0), prompt='9: ',restricted = 'Ee', correctans = 'Ee' , x=373, y = 96)
        txtbx58 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Rr', correctans = 'Rr' , x=406, y = 96)
        txtbx59 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Cc', correctans = 'Cc' , x=418, y = 96)
        txtbx60 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Yy', correctans = 'Yy' , x=430, y = 96)
        #Down10(DracoMalfoy (y) is in Deathly(Across5 #36))
        txtbx61 = eztext.Input(maxlength=1, color=(0,0,0), prompt='10: ',restricted = 'Dd', correctans = 'Dd' , x=211, y = 96)
        txtbx62 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ',restricted = 'Rr', correctans = 'Rr' , x=226, y = 108)
        txtbx63 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Aa', correctans = 'Aa' , x=226, y = 120)
        txtbx64 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Cc', correctans = 'Cc' ,x=226, y = 132)
        txtbx65 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Oo', correctans = 'Oo' ,x=226, y = 144)
        txtbx66 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Mm', correctans = 'Mm' ,x=226, y = 156)
        txtbx67 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Aa', correctans = 'Aa' ,x=226, y = 168)
        txtbx68 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Ll', correctans = 'Ll' ,x=226, y = 180)
        txtbx69 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Ff', correctans = 'Ff' ,x=226, y = 192)
        txtbx70 = eztext.Input(maxlength=1, color=(0,0,0), prompt=' ', restricted = 'Oo', correctans = 'Oo' ,x=226, y = 204)

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

                Question1 = font2.render("1. The only Weasley that did not fight for the Order at the Battle of Hogwarts", True, (0, 0, 0))
                screen.blit(Question1,(205 - Question1.get_width() // 2, 400 - Question1.get_height() // 2))

                Question2 = font2.render("2. Tri Wizard Tournament contestant that married Bill Weasley", True, (0, 0, 0))
                screen.blit(Question2,(170 - Question2.get_width() // 2, 550 - Question2.get_height() // 2))

                Question3 = font2.render("3. To close the 'Mauraders Map' you say: ", True, (0, 0, 0))
                screen.blit(Question3,(114 - Question3.get_width() // 2, 415 - Question3.get_height() // 2))

                Question4 = font2.render("4. How many Horcrux's did Voldemort create (including Harry)", True, (0, 0, 0))
                screen.blit(Question4,(170 - Question4.get_width() // 2, 565 - Question4.get_height() // 2))

                Question5 = font2.render("5. The first friend Harry makes at Hogwarts", True, (0, 0, 0))
                screen.blit(Question5,(118 - Question5.get_width() // 2, 430 - Question5.get_height() // 2))

                Question6 = font2.render("6. Hogwarts house containing the colors Blue and Silver", True, (0, 0, 0))
                screen.blit(Question6,(155 - Question6.get_width() // 2, 580 - Question6.get_height() // 2))

                Question7 = font2.render("7. The Horcrux destroyed by Neville", True, (0, 0, 0))
                screen.blit(Question7,(100 - Question7.get_width() // 2, 445 - Question7.get_height() // 2))

                Question8 = font2.render("8. The Horcrux tied to Rowena Ravenclaw", True, (0, 0, 0))
                screen.blit(Question8,(117 - Question8.get_width() // 2, 595 - Question8.get_height() // 2))

                Question9 = font2.render("9. What does the Invisiblity cloak, Elder wand and Resurection stone combined together make?", True, (0, 0, 0))
                screen.blit(Question9,(260 - Question9.get_width() // 2, 460 - Question9.get_height() // 2))

                Question10 = font2.render("10. Who was chosen by Voldemort to kill Dumbledore", True, (0, 0, 0))
                screen.blit(Question10,(145 - Question10.get_width() // 2, 610 - Question10.get_height() // 2))


                #Across1
                textandrectangle(311,120,txtbx1,events)
                textandrectangle(323,120,txtbx2,events)
                textandrectangle(335,120,txtbx3,events)
                #Down2
                textandrectangle(335,72,txtbx4,events)
                textandrectangle(335,84,txtbx5,events)
                textandrectangle(335,96,txtbx6,events)
                textandrectangle(335,108,txtbx7,events)

                #Across3
                textandrectangle(311,72,txtbx8,events)
                textandrectangle(323,72,txtbx9,events)
                textandrectangle(347,72,txtbx10,events)
                textandrectangle(359,72,txtbx11,events)
                textandrectangle(371,72,txtbx12,events)
                textandrectangle(383,72,txtbx13,events)
                textandrectangle(395,72,txtbx14,events)
                textandrectangle(407,72,txtbx15,events)
                textandrectangle(419,72,txtbx16,events)
                textandrectangle(431,72,txtbx17,events)
                textandrectangle(443,72,txtbx18,events)
                textandrectangle(455,72,txtbx19,events)
                textandrectangle(467,72,txtbx20,events)
                textandrectangle(479,72,txtbx21,events)

                #Down4
                textandrectangle(311,132,txtbx22,events)
                textandrectangle(311,144,txtbx23,events)
                textandrectangle(311,156,txtbx24,events)
                textandrectangle(311,168,txtbx25,events)
                textandrectangle(311,180,txtbx26,events)
                textandrectangle(311,192,txtbx27,events)
                textandrectangle(311,204,txtbx28,events)
                textandrectangle(311,216,txtbx29,events)

                #Across5
                textandrectangle(167,216,txtbx30,events)
                textandrectangle(179,216,txtbx31,events)
                textandrectangle(191,216,txtbx32,events)
                textandrectangle(203,216,txtbx33,events)
                textandrectangle(215,216,txtbx34,events)
                textandrectangle(227,216,txtbx35,events)
                textandrectangle(239,216,txtbx36,events)
                textandrectangle(251,216,txtbx37,events)
                textandrectangle(263,216,txtbx38,events)
                textandrectangle(275,216,txtbx39,events)
                textandrectangle(287,216,txtbx40,events)
                textandrectangle(299,216,txtbx41,events)
                textandrectangle(323,216,txtbx42,events)

                #Down6
                textandrectangle(395,84,txtbx43,events)
                textandrectangle(395,96,txtbx44,events)
                textandrectangle(395,108,txtbx45,events)
                textandrectangle(395,120,txtbx46,events)

                #Across7
                textandrectangle(323,168,txtbx47,events)
                textandrectangle(335,168,txtbx48,events)
                textandrectangle(347,168,txtbx49,events)
                textandrectangle(359,168,txtbx50,events)
                textandrectangle(371,168,txtbx51,events)

                #Down8
                textandrectangle(467,84,txtbx52,events)
                textandrectangle(467,96,txtbx53,events)
                textandrectangle(467,108,txtbx54,events)
                textandrectangle(467,120,txtbx55,events)
                textandrectangle(467,132,txtbx56,events)

                #Across9
                textandrectangle(383,96,txtbx57,events)
                textandrectangle(407,96,txtbx58,events)
                textandrectangle(419,96,txtbx59,events)
                textandrectangle(431,96,txtbx60,events)

                #Down10
                textandrectangle(227,96,txtbx61,events)
                textandrectangle(227,108,txtbx62,events)
                textandrectangle(227,120,txtbx63,events)
                textandrectangle(227,132,txtbx64,events)
                textandrectangle(227,144,txtbx65,events)
                textandrectangle(227,156,txtbx66,events)
                textandrectangle(227,168,txtbx67,events)
                textandrectangle(227,180,txtbx68,events)
                textandrectangle(227,192,txtbx69,events)
                textandrectangle(227,204,txtbx70,events)

                pygame.display.flip()
                clock.tick(30)
        pygame.display.quit


if __name__ == '__main__':Board()
