#snake game
import time
def clearscreen():
    print('\n'*50)
clearscreen()
name = input('enter your name')
def p(line):
    print('|'+str(line)+'|')
def printarena():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18, direction
    print('_'*100)
    p(l18),p(l17),p(l16),p(l15),p(l14),p(l13),p(l12),p(l11),p(l10),p(l9),p(l8),p(l7),p(l6),p(l5),p(l4),p(l3),p(l2),p(l1)
    print('_'*100)
    print(direction)
def removeball():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18
    l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = l1.replace('o',' '),l2.replace('o',' '),l3.replace('o',' '),l4.replace('o',' '),l5.replace('o',' '),l6.replace('o',' '),l7.replace('o',' '),l8.replace('o',' '),l9.replace('o',' '),line10.replace('o',' '),l11.replace('o',' '),l12.replace('o',' '),l13.replace('o',' '),l14.replace('o',' '),l15.replace('o',' '),l16.replace('o',' '),l17.replace('o',' '),l18.replace('o',' ')
def removeballatleft(linescan):
    scanner,counter,toreturn = '',0,''
    while scanner != 'o':
        scanner = linescan[counter]
        toreturn = toreturn + scanner
        counter += 1
    toreturn = toreturn + linescan[counter:]
    return toreturn
def removeballatright(linescan):
    scanner,counter,toreturn = '',99,''
    while scanner != 'o':
        scanner = linescan[counter]
        toreturn = scanner + toreturn
        counter -= 1
    toreturn = linescan[:counter] + toreturn
    return toreturn
def removeballfrombottom():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18
    ln = 1 if ('o' in l1 ) else (2 if ('o' in l2 ) else (3 if ('o' in l3 ) else (4 if ('o' in l4 ) else (5 if ('o' in l5 ) else (6 if ('o' in l6 ) else (7 if ('o' in l7 ) else (8 if ('o' in l8 ) else (9 if ('o' in l9 ) else (10 if ('o' in l10 ) else (11 if ('o' in l11 ) else (12 if ('o' in l12 ) else (13 if ('o' in l13 ) else (14 if ('o' in l14 ) else (15 if ('o' in l15 ) else (16 if ('o' in l16 ) else (17 if ('o' in l17 ) else 18))))))))))))))))
    #l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = (removeball(l1) if ln == 1 else l1)
def addballattop():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18
    ln = 18 if ('o' in l18 ) else (17 if ('o' in l17 ) else (16 if ('o' in l16 ) else (15 if ('o' in l15 ) else (114 if ('o' in l14 ) else (13 if ('o' in l13 ) else (12 if ('o' in l12 ) else (11 if ('o' in l11 ) else (10 if ('o' in l10 ) else (9 if ('o' in l9 ) else (8 if ('o' in l8 ) else (7 if ('o' in l7 ) else (6 if ('o' in l6 ) else (5 if ('o' in l5 ) else (4 if ('o' in l4 ) else (3 if ('o' in l3 ) else (2 if ('o' in l2 ) else 1))))))))))))))))
    l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = (addball(l2) if ln == 1 else l2),(addball(l3) if ln == 2 else l3),(addball(l4) if ln == 3 else l4),(addball(l5) if ln == 4 else l5),(addball(l6) if ln == 5 else l6),(addball(l7) if ln == 6 else l7),(addball(l8) if ln == 7 else l8),(addball(l9) if ln == 8 else l9),(addball(l10) if ln == 9 else l10),(addball(l11) if ln == 10 else l11),(addball(l12) if ln == 11 else l2),(addball(l3) if ln == 12 else l3),(addball(l14) if ln == 13 else l14),(addball(l15) if ln == 14 else l15),(addball(l16) if ln == 15 else l16),(addball(l17) if ln == 16 else l7),(addball(l18) if ln == 17 else l18)
def addball(line):
    global pos
    linepart1 = line[:pos-1]
    linepart2 = line[pos+5:]
    line = linepart1 + 'o' + linepart2
    return line
pos = 50
l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = ' '*99,' '*99,' '*99,' '*99,' '*99,' '*99,' '*99,' '*99,' '*99,' '*99,((' '*4)+'o'+(' '*90)),' '*99,' '*99,' '*99,' '*99,' '*99,' '*99,' '*99
direction = 'right'
turningmode = False
while True:
    try:
        time.sleep(0.1)
        printarena()
        ln = 1 if ('o' in l1 ) else (2 if ('o' in l2 ) else (3 if ('o' in l3 ) else (4 if ('o' in l4 ) else (5 if ('o' in l5 ) else (6 if ('o' in l6 ) else (7 if ('o' in l7 ) else (8 if ('o' in l8 ) else (9 if ('o' in l9 ) else (10 if ('o' in l10 ) else (11 if ('o' in l11 ) else (12 if ('o' in l12 ) else (13 if ('o' in l13 ) else (14 if ('o' in l14 ) else (15 if ('o' in l15 ) else (16 if ('o' in l16 ) else (17 if ('o' in l17 ) else 18))))))))))))))))
        if turningmode == True:
            blank = ''
            #turn
        else:
            ln = 1 if ('o' in l1 ) else (2 if ('o' in l2 ) else (3 if ('o' in l3 ) else (4 if ('o' in l4 ) else (5 if ('o' in l5 ) else (6 if ('o' in l6 ) else (7 if ('o' in l7 ) else (8 if ('o' in l8 ) else (9 if ('o' in l9 ) else (10 if ('o' in l10 ) else (11 if ('o' in l11 ) else (12 if ('o' in l12 ) else (13 if ('o' in l13 ) else (14 if ('o' in l14 ) else (15 if ('o' in l15 ) else (16 if ('o' in l16 ) else (17 if ('o' in l17 ) else 18))))))))))))))))
            if direction == 'right':
                pos,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = pos+1,(' '+l1[:99] if 'o' in l1 else l1),(' '+l2[:99] if 'o' in l2 else l2),(' '+l3[:99] if 'o' in l3 else l3),(' '+l4[:99] if 'o' in l4 else l4),(' '+l5[:99] if 'o' in l5 else l5),(' '+l6[:99] if 'o' in l6 else l6),(' '+l7[:99] if 'o' in l7 else l7),(' '+l8[:99] if 'o' in l8 else l8),(' '+l9[:99] if 'o' in l9 else l9),(' '+l10[:99] if 'o' in l10 else l10),(' '+l11[:99] if 'o' in l11 else l11),(' '+l12[:99] if 'o' in l12 else l12),(' '+l13[:99] if 'o' in l13 else l13),(' '+l14[:99] if 'o' in l14 else l14),(' '+l15[:99] if 'o' in l15 else l15),(' '+l16[:99] if 'o' in l16 else l16),(' '+l17[:99] if 'o' in l17 else l17),(' '+l18[:99] if 'o' in l18 else l18)
            if direction == 'left':
                pos,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = pos-1,(l1[1:]+' ' if 'o' in l1 else l1),(l2[1:]+' 'if 'o' in l2 else l2),(l3[1:]+' ' if 'o' in l3 else l3),(l4[1:]+' ' if 'o' in l4 else l4),(l5[1:]+' ' if 'o' in l5 else l5),(l6[1:]+' ' if 'o' in l6 else l6),(l7[1:]+' ' if 'o' in l7 else l7),(l8[1:]+' ' if 'o' in l8 else l8),(l9[1:]+' ' if 'o' in l9 else l9),(' '+l10[1:]+' ' if 'o' in l10 else l10),(l11[1:]+' ' if 'o' in l11 else l11),(l12[1:]+' ' if 'o' in l12 else l12),(l13[1:]+' ' if 'o' in l13 else l13),(l14[1:]+' ' if 'o' in l14 else l14),(l15[1:]+' ' if 'o' in l15 else l15),(l16[1:]+' ' if 'o' in l16 else l16),(l17[1:]+' ' if 'o' in l17 else l17),(l18[1:]+' ' if 'o' in l18 else l18)
            if direction == 'up':
                removeball()
                l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l6,l17,l18 = (addball(l2) if ln == 1 else l2),(addball(l3) if ln == 2 else l3),(addball(l4) if ln == 3 else l4),(addball(l5) if ln == 4 else l5),(addball(l6) if ln == 5 else l6),(addball(l7) if ln == 6 else l7),(addball(l8) if ln == 7 else l8),(addball(l9) if ln == 8 else l9),(addball(l10) if ln == 9 else l10),(addball(l11) if ln == 10 else l11),(addball(l12) if ln == 11 else l12),(addball(l13) if ln == 12 else l13),(addball(l14) if ln == 13 else l14),(addball(l15) if ln == 14 else l15),(addball(l16) if ln == 15 else l16),(addball(l17) if ln == 16 else l17),(addball(l18) if ln == 17 else l18)
            if direction == 'down':
                removeball()
                l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l6,l17 = (addball(l1) if ln == 2 else l1),(addball(l2) if ln == 3 else l2),(addball(l3) if ln == 4 else l3),(addball(l4) if ln == 5 else l4),(addball(l5) if ln == 6 else l5),(addball(l6) if ln == 7 else l6),(addball(l7) if ln == 8 else l7),(addball(l8) if ln == 9 else l8),(addball(l9) if ln == 10 else l9),(addball(l10) if ln == 11 else l10),(addball(l11) if ln == 12 else l11),(addball(l12) if ln == 13 else l12),(addball(l13) if ln == 14 else l13),(addball(l14) if ln == 15 else l14),(addball(l15) if ln == 16 else l15),(addball(l16) if ln == 17 else l16),(addball(l17) if ln == 18 else l17)
            #if direction == 'up':
                #l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = (removeball(l1) if ln == 1 else l1), (removeball(l2) if ln == 2 else l2),(removeball(l3) if ln == 3 else l3),(removeball(l4) if ln == 4 else l4),(removeball(l5) if ln == 5 else l5),(removeball(l6) if ln == 6 else (addball if ln == 1 else l6)),(removeball(l7) if ln == 7 else (addball if ln == 2 else l7)),(removeball(l8) if ln == 8 else (addball if ln == 3 else l8)),(removeball(l9) if ln == 9 else (addball if ln == 4 else l9)),(removeball(l10) if ln == 10 else (addball if ln == 5 else l10)),(removeball(l11) if ln == 11 else (addball if ln == 6 else l11)),(removeball(l12) if ln == 12 else (addball if ln == 7 else l12)),(removeball(l13) if ln == 13 else (addball if ln == 8 else l13)),(removeball(l14) if ln == 14 else (addball if ln == 9 else l14)),(removeball(l15) if ln == 15 else (addball if ln == 10 else l15)),(removeball(l16) if ln == 16 else (addball if ln == 11 else l16)),(removeball(l17) if ln == 17 else (addball if ln == 12 else l17)),(removeball(18) if ln == 18 else (addball if ln == 13 else l18))
            #if direction == 'down':
                #l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = (addball(l1) if ln == 1 else l1),(addball(l2) if ln == 2 else l2),(addball(l3) if ln == 3 else l3),(addball(l4) if ln == 4 else l4),(addball(l5) if ln == 5 else l5),(addball(l6) if ln == 6 else (removeball if ln == 1 else l6)),(addball(l7) if ln == 7 else (removeball if ln == 2 else l7)),(addball(l8) if ln == 8 else (removeball if ln == 3 else l8)),(addball(l9) if ln == 9 else (removeball if ln == 4 else l9)),(addball(l10) if ln == 10 else (removeball if ln == 5 else l10)),(addball(l11) if ln == 11 else (removeball if ln == 6 else l11)),(addball(l12) if ln == 12 else (removeball if ln == 7 else l12)),(addball(l13) if ln == 13 else (removeball if ln == 8 else l13)),(addball(l14) if ln == 14 else (removeball if ln == 9 else l14)),(addball(l15) if ln == 15 else (removeball if ln == 10 else l15)),(addball(l16) if ln == 16 else (removeball if ln == 11 else l16)),(addball(l17) if ln == 17 else (removeball if ln == 12 else l17)),(addball(l18) if ln == 18 else (removeball if ln == 13 else l18))
    except:
        ln = 1 if ('o' in l1 ) else (2 if ('o' in l2 ) else (3 if ('o' in l3 ) else (4 if ('o' in l4 ) else (5 if ('o' in l5 ) else (6 if ('o' in l6 ) else (7 if ('o' in l7 ) else (8 if ('o' in l8 ) else (9 if ('o' in l9 ) else (10 if ('o' in l10 ) else (11 if ('o' in l11 ) else (12 if ('o' in l12 ) else (13 if ('o' in l13 ) else (14 if ('o' in l14 ) else (15 if ('o' in l15 ) else (16 if ('o' in l16 ) else (17 if ('o' in l17 ) else 18))))))))))))))))
        lcont = l1 if ('o' in l1 ) else (l2 if ('o' in l2 ) else (l3 if ('o' in l3 ) else (l4 if ('o' in l4 ) else (l5 if ('o' in l5 ) else (l6 if ('o' in l6 ) else (l7 if ('o' in l7 ) else (l8 if ('o' in l8 ) else (l9 if ('o' in l9 ) else (l10 if ('o' in l10 ) else (l11 if ('o' in l11 ) else (l12 if ('o' in l12 ) else (l13 if ('o' in l13 ) else (l14 if ('o' in l14 ) else (l15 if ('o' in l15 ) else (l16 if ('o' in l16 ) else (l17 if ('o' in l17 ) else l18))))))))))))))))
        lcontbelow = l1 if ('o' in l1 ) else (l1 if ('o' in l2 ) else (l2 if ('o' in l3 ) else (l4 if ('o' in l5 ) else (l5 if ('o' in l6 ) else (l6 if ('o' in l7 ) else (l7 if ('o' in l8 ) else (l8 if ('o' in l9 ) else (l9 if ('o' in l10 ) else (l10 if ('o' in l11 ) else (l11 if ('o' in l12 ) else (l12 if ('o' in l13 ) else (l13 if ('o' in l14 ) else (l14 if ('o' in l15 ) else (l15 if ('o' in l16 ) else (l16 if ('o' in l17 ) else (l17 if ('o' in l18 ) else l18))))))))))))))))
        lcontabove = l2 if ('o' in l1 ) else (l3 if ('o' in l2 ) else (l4 if ('o' in l3 ) else (l5 if ('o' in l4 ) else (l6 if ('o' in l5 ) else (l7 if ('o' in l6 ) else (l8 if ('o' in l7 ) else (l9 if ('o' in l8 ) else (l10 if ('o' in l9 ) else (l11 if ('o' in l10 ) else (l12 if ('o' in l11 ) else (l13 if ('o' in l12 ) else (l14 if ('o' in l13 ) else (l15 if ('o' in l14 ) else (l16 if ('o' in l15 ) else (l16 if ('o' in l16 ) else (l18 if ('o' in l17 ) else l18))))))))))))))))
        if direction == 'right':
            direction = 'down'
        elif direction == 'down':
            direction = 'left'
        elif direction == 'left':
            direction = 'up'
        else:
            direction = 'right'
        #up and down have problems

            




            