import pygame
from network import Network

pygame.font.init()

white = (255,255,255)
black = (0,0,0)
width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
run = True

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

btns = [Button("Comenzar Partida", 50, 500, white)]

def redrawWindow(win, game, p):
    win.fill(black)

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, white, True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)

        text = font.render("Tu Carta", 1, (0, 255,255))
        win.blit(text, (80, 200))

        text = font.render("Oponente", 1, (0, 255, 255))
        win.blit(text, (380, 200))

        if not game.p1Went and p == 0:
            text = font.render("Tu turno", 1, white)
            win.blit(text, (80, 200))
        elif not game.p2Went and p == 1:
            text = font.render("Esperando...", 1, white)
            win.blit(text, (80, 200))
        
        for btn in btns:
            btn.draw(win)

    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            pygame.display.update()
            pygame.time.delay(2000)

def menu_screen():
    print("menu screen started")
    clock = pygame.time.Clock()
    global run
    while run:
        clock.tick(60)
        win.fill(black)
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render("Click to Play!", 1, (255,255,255))
        win.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                print("exit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                main()

# Ejecucion
while run:
    menu_screen()
