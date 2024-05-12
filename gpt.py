import pygame
import time
import random

pygame.init()

# Ustawienia okna gry
szerokosc = 800
wysokosc = 600
rozmiar_bloczka = 10

# Kolory
bialy = (255, 255, 255)
czarny = (0, 0, 0)
zielony = (0, 255, 0)
czerwony = (255, 0, 0)

# Inicjalizacja okna gry
okno_gry = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption('Snake Game')


# Funkcja rysująca węża na planszy
def rysuj_weza(waz, rozmiar_bloczka):
    for blok in waz:
        pygame.draw.rect(okno_gry, zielony, [blok[0], blok[1], rozmiar_bloczka, rozmiar_bloczka])


# Funkcja główna gry
def gra():
    # Pozycja startowa węża
    waz = [[szerokosc / 2, wysokosc / 2]]
    kierunek = 'DOL'

    # Pozycja startowa jedzenia
    jedzenie_x = round(random.randrange(0, szerokosc - rozmiar_bloczka) / 10.0) * 10.0
    jedzenie_y = round(random.randrange(0, wysokosc - rozmiar_bloczka) / 10.0) * 10.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Obsługa kierunku węża
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            kierunek = 'LEWO'
        elif keys[pygame.K_RIGHT]:
            kierunek = 'PRAWO'
        elif keys[pygame.K_UP]:
            kierunek = 'GORA'
        elif keys[pygame.K_DOWN]:
            kierunek = 'DOL'

        if kierunek == 'LEWO':
            waz[0][0] -= rozmiar_bloczka
        elif kierunek == 'PRAWO':
            waz[0][0] += rozmiar_bloczka
        elif kierunek == 'GORA':
            waz[0][1] -= rozmiar_bloczka
        elif kierunek == 'DOL':
            waz[0][1] += rozmiar_bloczka

        # Sprawdzenie czy wąż zjadł jedzenie
        if waz[0][0] == jedzenie_x and waz[0][1] == jedzenie_y:
            waz.append([])
            jedzenie_x = round(random.randrange(0, szerokosc - rozmiar_bloczka) / 10.0) * 10.0
            jedzenie_y = round(random.randrange(0, wysokosc - rozmiar_bloczka) / 10.0) * 10.0

        # Rysowanie tła
        okno_gry.fill(bialy)

        # Rysowanie węża
        rysuj_weza(waz, rozmiar_bloczka)

        # Rysowanie jedzenia
        pygame.draw.rect(okno_gry, czerwony, [jedzenie_x, jedzenie_y, rozmiar_bloczka, rozmiar_bloczka])

        pygame.display.update()
        time.sleep(0.1)


gra()