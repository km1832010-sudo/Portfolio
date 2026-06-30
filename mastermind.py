from graphics import *
import random

def game():
    win = GraphWin("Window", 400, 400)
    win.setCoords(0, 0, 400, 400)
    win.setBackground("grey")

    pallet1 = Circle(Point(120, 15), 10)
    pallet1.draw(win)
    pallet1.setFill("red")

    pallet2 = Circle(Point(150, 15) , 10)
    pallet2.draw(win)
    pallet2.setFill("orange")

    pallet3 = Circle(Point(180, 15) , 10)
    pallet3.draw(win)
    pallet3.setFill("yellow")

    pallet4 = Circle(Point(210, 15) , 10)
    pallet4.draw(win)
    pallet4.setFill("green")

    pallet5 = Circle(Point(240, 15) , 10)
    pallet5.draw(win)
    pallet5.setFill("blue")

    pallet6 = Circle(Point(270, 15) , 10)
    pallet6.draw(win)
    pallet6.setFill("purple")

    colorpallet=["red","orange","yellow","green","blue","purple"]

    delete= Rectangle(Point(0,0), Point(80,40))
    delete.draw(win)
    delete.setFill("lightblue")
    deletetext= Text(Point(40,20),"DELETE")
    deletetext.draw(win)

    guesss = Rectangle(Point(0, 40), Point(80, 80))
    guesss.draw(win)
    guesss.setFill("lightblue")
    guessstext = Text(Point(40, 60), "GUESS")
    guessstext.draw(win)

    restart= Rectangle(Point(0,360), Point(80,400))
    restart.draw(win)
    restart.setFill("lightblue")
    restarttext= Text(Point(40,380),"RESTART")
    restarttext.draw(win)

    quit1 = Rectangle(Point(400, 0), Point(320, 40))
    quit1.draw(win)
    quit1.setFill("lightblue")
    quittext = Text(Point(360, 20), "QUIT")
    quittext.draw(win)

    info = Rectangle(Point(360, 360), Point(400, 400))
    info.draw(win)
    info.setFill("lightblue")
    infotext = Text(Point(380, 380), "?")
    infotext.draw(win)

    for y in range(6):
        line=Line(Point(135+ (y*30),30),Point(135+ (y*30),300))
        line.draw(win)

    for w in range(10):
        line = Line(Point(135, 30+ (w*30)), Point(285, 30 + (w*30)))
        line.draw(win)

    for r in range(1,9):
        nums= Text(Point(125, 15 + (30*r)), str(r) + ":")
        nums.draw(win)

    ai = Text(Point(125, 15 + (30 * 9)), "AI:")
    ai.draw(win)

    computer=[]
    for i in range(1,5):
        computer.append(random.choice(colorpallet))

    def gameround():
        player = []
        def playerguess():
            while True:
                guesses = len(player)
                click = win.getMouse()
                xcoord = click.getX()
                ycoord = click.getY()
                distance1 = ((xcoord -120) ** 2 + (ycoord -15) ** 2) ** 0.5
                distance2 = ((xcoord -150) ** 2 + (ycoord -15) ** 2) ** 0.5
                distance3 = ((xcoord -180) ** 2 + (ycoord -15) ** 2) ** 0.5
                distance4 = ((xcoord -210) ** 2 + (ycoord -15) ** 2) ** 0.5
                distance5 = ((xcoord -240) ** 2 + (ycoord -15) ** 2) ** 0.5
                distance6 = ((xcoord -270) ** 2 + (ycoord -15) ** 2) ** 0.5
                if distance1<=10:
                    x="red"
                    player.append(x)
                    return x
                elif distance2<=10:
                    x="orange"
                    player.append(x)
                    return x
                elif distance3<=10:
                    x="yellow"
                    player.append(x)
                    return x
                elif distance4<=10:
                    x="green"
                    player.append(x)
                    return x
                elif distance5<=10:
                    x="blue"
                    player.append(x)
                    return x
                elif distance6<=10:
                    x="purple"
                    player.append(x)
                    return x
                elif click.getX()<=80 and click.getY()<=40:
                    if guesses==0:
                        continue
                    elif guesses==1:
                        player.remove(player[0])
                        g11()
                    elif guesses==2:
                        player.remove(player[1])
                        g22()
                    elif guesses==3:
                        player.remove(player[2])
                        g33()
                elif click.getX() <= 80 and click.getY() >= 360:
                    win.close()
                    game()
                elif click.getX() >= 320 and click.getY() <= 40:
                    exit()
                elif click.getX() >= 360 and click.getY() >= 360:
                    open = False
                    if not open:
                        win2 = GraphWin("Info", 400, 400)
                        win2.setCoords(0, 0, 400, 400)
                        win2.setBackground("brown")

                        infotext21 = Text(Point(200, 380),
                                         "MasterMind game rules:The computer has selected a ")
                        infotext21.draw(win2)

                        infotext22 = Text(Point(200, 360),
                                         "secret combination of 4 colored pegs and you have to")
                        infotext22.draw(win2)

                        infotext23 = Text(Point(200, 340),
                                         "guess that combination in 8 or fewer tries to win. To c-")
                        infotext23.draw(win2)

                        infotext24 = Text(Point(200, 320),
                                          "reate your guess click each apparent colored peg until")
                        infotext24.draw(win2)

                        infotext25 = Text(Point(200, 300),
                                          "you've filled the row with your combination (you can  ")
                        infotext25.draw(win2)

                        infotext26 = Text(Point(200, 280),
                                          "delete your guess by clicking (delete) button).Then cl-")
                        infotext26.draw(win2)

                        infotext27 = Text(Point(200, 260),
                                          "ick the check button. Each time you submit a guess the")
                        infotext27.draw(win2)

                        infotext28 = Text(Point(200, 240),
                                          "machine will use score pegs to let you know how close ")
                        infotext28.draw(win2)

                        infotext29 = Text(Point(200, 220),
                                          "that guess is. For each guess a black score peg indi-")
                        infotext29.draw(win2)

                        infotext30 = Text(Point(200, 200),
                                          "cates that one of your pegs is the right color in the right")
                        infotext30.draw(win2)

                        infotext31 = Text(Point(200, 180),
                                          "position. A white score peg indicates that one of your")
                        infotext31.draw(win2)

                        infotext32 = Text(Point(200, 160),
                                          "pegs is the right color in the wrong position. Use the")
                        infotext32.draw(win2)

                        infotext33 = Text(Point(200, 140),
                                          "score to guide your next guess. If you guess 4 black")
                        infotext33.draw(win2)

                        infotext34 = Text(Point(200, 120),
                                          "pegs within 8 tries, you win. To begin a new game click")
                        infotext34.draw(win2)

                        infotext35 = Text(Point(200, 100),
                                          "the restart button.")
                        infotext35.draw(win2)

                        open= True

                        close = Rectangle(Point(160, 0), Point(240, 40))
                        close.draw(win2)
                        close.setFill("lightBlue")
                        closetext = Text(Point(200, 20), "CLOSE")
                        closetext.draw(win2)
                        while True:
                            click2 = win2.getMouse()
                            xcoord2 = click2.getX()
                            ycoord2 = click2.getY()
                            if xcoord2 >= 160 and xcoord2 <= 240 and ycoord2 >= 0 and ycoord2 <= 40:
                                win2.close()
                                break

                    elif open:
                        continue

        def g1():
            guess1 = Circle(Point(150, (30 * d) + 15), 10)
            guess1.setFill(playerguess())
            guess1.draw(win)
        def g2():
            guess2 = Circle(Point(180, (30 * d) + 15), 10)
            guess2.setFill(playerguess())
            guess2.draw(win)
        def g3():
            guess3 = Circle(Point(210, (30 * d) + 15), 10)
            guess3.setFill(playerguess())
            guess3.draw(win)
        def g4():
            guess4 = Circle(Point(240, (30 * d) + 15), 10)
            guess4.setFill(playerguess())
            guess4.draw(win)

        def g11():
            guess11 = Circle(Point(150, (30 * d) + 15), 10)
            guess11.setFill("grey")
            guess11.draw(win)
            guess11.setFill(playerguess())
            guess11.undraw()
            guess11.draw(win)
        def g22():
            guess22 = Circle(Point(180, (30 * d) + 15), 10)
            guess22.setFill("grey")
            guess22.draw(win)
            guess22.setFill(playerguess())
            guess22.undraw()
            guess22.draw(win)
        def g33():
            guess33 = Circle(Point(210, (30 * d) + 15), 10)
            guess33.setFill("grey")
            guess33.draw(win)
            guess33.setFill(playerguess())
            guess33.undraw()
            guess33.draw(win)
        def g44():
            guess44 = Circle(Point(240, (30 * d) + 15), 10)
            guess44.setFill("grey")
            guess44.draw(win)
            guess44.setFill(playerguess())
            guess44.undraw()
            guess44.draw(win)


        g1()
        g2()
        g3()
        g4()


        while True:
            click = win.getMouse()
            xcoord = click.getX()
            ycoord = click.getY()
            if click.getX() <= 80 and click.getY() >= 40 and click.getY() <= 80:

                feedback1 = Circle(Point(265, (30 * d) + 20), 5)
                feedback2 = Circle(Point(275, (30 * d) + 20), 5)
                feedback3 = Circle(Point(265, (30 * d) + 10), 5)
                feedback4 = Circle(Point(275, (30 * d) + 10), 5)
                whiteantidupe = []
                blackantidupe = []
                total = 0

                white = []
                black = []
                clear = []
                feedback = []
                for k in range(0, 4):
                    if player[k] == computer[k]:
                        total += 1
                        black.append("black")
                        blackantidupe.append(player[k])
                        if player[k] in whiteantidupe:
                            z = whiteantidupe.count(player[k])
                            for zs in range(0, z):
                                whiteantidupe.remove(player[k])
                                white.pop()
                            clear.append("grey")
                            blackantidupe.append(player[k])
                    elif player[k] in whiteantidupe or player[k] in blackantidupe:
                        clear.append("grey")
                    elif player[k] in computer:
                        whiteantidupe.append(player[k])
                        white.append("white")
                    else:
                        clear.append("grey")
                for j in range(0, len(black)):
                    feedback.append(black[j])
                for a in range(0, len(white)):
                    feedback.append(white[a])
                for b in range(0, len(clear)):
                    feedback.append(clear[b])

                feedback1.setFill(feedback[0])
                feedback2.setFill(feedback[1])
                feedback3.setFill(feedback[2])
                feedback4.setFill(feedback[3])
                feedback1.draw(win)
                feedback2.draw(win)
                feedback3.draw(win)
                feedback4.draw(win)

                if total == 4:
                    result = Text(Point(195, 380), "You Win!!!")
                    result.draw(win)
                    return 2
                break
            elif click.getX() <= 80 and click.getY() <= 40:
                player.remove(player[3])
                g44()

    def printcomp():
        computer1 = Circle(Point(150, 285), 10)
        computer2 = Circle(Point(180, 285), 10)
        computer3 = Circle(Point(210, 285), 10)
        computer4 = Circle(Point(240, 285), 10)

        computer1.setFill(computer[0])
        computer2.setFill(computer[1])
        computer3.setFill(computer[2])
        computer4.setFill(computer[3])

        computer1.draw(win)
        computer2.draw(win)
        computer3.draw(win)
        computer4.draw(win)

    for d in range(1, 9):
        if gameround() == 2:
            for p in range(2, 10):
                circ1 = Circle(Point(150, (30 * p) + 15), 10)
                circ2 = Circle(Point(180, (30 * p) + 15), 10)
                circ3 = Circle(Point(210, (30 * p) + 15), 10)
                circ4 = Circle(Point(240, (30 * p) + 15), 10)

                circ1.draw(win)
                circ2.draw(win)
                circ3.draw(win)
                circ4.draw(win)

                printcomp()
        elif d==8:
            result = Text(Point(195, 380), "You Lose!!!")
            result.draw(win)

    printcomp()

    while True:
        click = win.getMouse()
        if click.getX() <= 80 and click.getY() >= 360:
            win.close()
            game()
        elif click.getX() >= 320 and click.getY() <= 40:
            exit()

game()