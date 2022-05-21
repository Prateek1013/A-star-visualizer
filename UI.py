from config import * 

def is_resetButton(MOUSEPOS):
    if 0 <= MOUSEPOS[0]  <= BUTTONWIDTH and HEIGHT <= MOUSEPOS[1] <= HEIGHT + BUTTONHEIGHT:
        return True
    return False

def is_quitButton(MOUSEPOS):
    if BUTTONWIDTH <= MOUSEPOS[0] <= 2 * BUTTONWIDTH and HEIGHT <= MOUSEPOS[1] <= HEIGHT + BUTTONHEIGHT:
        return True
    return False

def is_matrixButton(MOUSEPOS):   
    if 0 <= MOUSEPOS[1] <= HEIGHT:
        return True
    return 
    
def is_randomButton(MOUSEPOS):   
    if 2 * BUTTONWIDTH <= MOUSEPOS[0] <= 7 * BUTTONWIDTH / 2 and HEIGHT <= MOUSEPOS[1] <= HEIGHT + BUTTONHEIGHT:
        return True
    return False

def is_selfButton(MOUSEPOS):   
    if 7 * BUTTONWIDTH / 2 <= MOUSEPOS[0] <= 9 * BUTTONWIDTH / 2 and HEIGHT <= MOUSEPOS[1] <= HEIGHT + BUTTONHEIGHT:
        print("self button is pressed")
        return True
    return False

def drawResetButton():
    pygame.draw.rect(SCREEN, GREY, (0, HEIGHT, BUTTONWIDTH, BUTTONHEIGHT))

def drawQuitButton():
    pygame.draw.rect(SCREEN, GREY, (BUTTONWIDTH, HEIGHT, BUTTONWIDTH, BUTTONHEIGHT))

def drawRandomButton():
    pygame.draw.rect(SCREEN, GREY, (2 * BUTTONWIDTH, HEIGHT, 3 * BUTTONWIDTH / 2, BUTTONHEIGHT))

def drawSelfButton():
    pygame.draw.rect(SCREEN, GREY, (7 * BUTTONWIDTH / 2, HEIGHT, BUTTONWIDTH, BUTTONHEIGHT))


