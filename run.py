#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys
import pygame
from pygame.locals import *
import random

import settings

# Constantes

# Clases
# ---------------------------------------------------------------------
class Cagna(pygame.sprite.Sprite):
    def __init__(self, cagna, group):
        super(Cagna, self).__init__(group)
        self.image = pygame.image.load(settings.IMAGES['cagna'])
        self.rect = self.image.get_rect()
        self.nombre = cagna['name']
        self.rect.x = cagna['x']
        self.rect.y = cagna['y']
        self.anzuelo = self.Anzuelo(self, group)
        self.tablero = Tablero(self)

    def update(self, pos):
        # Mover
        self.rect.x, self.rect.y = pos
        self.anzuelo.set_pos()
        self.peces = Peces(self)
        

    class Anzuelo(pygame.sprite.Sprite):
        def __init__(self, cagna, group):
            super(Cagna.Anzuelo, self).__init__(group)
            self.cagna = cagna
            self.image = pygame.image.load(settings.IMAGES['anzuelo'])
            self.rect = self.image.get_rect()
            self.set_pos()

        def set_pos(self):
            self.rect.x = self.cagna.rect.left
            self.rect.y = self.cagna.rect.bottom - self.rect.h

class Cagnas(pygame.sprite.Group):
    def __init__(self, **kwargs):
        super(Cagnas, self).__init__(**kwargs)


class Pez(pygame.sprite.Sprite):
    def __init__(self, pos, color, group):
        super(Pez, self).__init__(group)
        self.image = pygame.image.load(settings.IMAGES['pez_%s' % color]  )
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.pescado = False

    def update(self, pos):
        if not self.pescado:
            self.rect.x += random.randint(-1, 1)
            self.rect.y += random.randint(-1, 1)
        

class Peces(pygame.sprite.Group):
    def __init__(self, group):
        super(Peces, self).__init__(group)


class Pool(pygame.sprite.Group):
    def __init__(self, **kwargs):
        super(Pool, self).__init__(**kwargs)
        self.image = pygame.image.load(settings.IMAGES['pool_background'])
        self.peces = Peces(self)
        self.create_peces()
        self.cagna = Cagna(settings.CAGNA, self)

    def create_peces(self):
        for row in settings.POOL_XYS:
            for pos in row:
                color = random.choice(settings.COLORS)
                self.peces.add(Pez(pos, color,  self))

    def update(self, pos, click):
        self.peces.update(pos)
        if pos:
            super(Pool, self).update(pos)
            # Pescar
            if click:
                pez = None
                for pez in self.peces:
                    if self.cagna.anzuelo.rect.colliderect(pez.rect):
                        break
                    pez = None
                if pez:
                    pez.add(self.cagna.tablero.group)
                    pez.remove(self.peces)
                    self.cagna.tablero.update(pez)


class Tablero:
    def __init__(self, cagna):
        self.group = TableroGroup()
        self.cagna = cagna
        self.ps = list(settings.PS)

    def update(self, pez):
        pez.rect.x, pez.rect.y = self.ps.pop()
        pez.pescado = True


class TableroGroup(pygame.sprite.Group):
    def __init__(self, **kwargs):
        super(TableroGroup, self).__init__(**kwargs)


## ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
def clear_callback(surf, rect):
        surf.blit(surf, rect, rect)

# ---------------------------------------------------------------------

def main():
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("Pesca Milagrosa")

    clock = pygame.time.Clock()
    pool = Pool()

    print (KEYDOWN, MOUSEMOTION, MOUSEBUTTONDOWN)
    while True:
        click = pos = None
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        event = pygame.event.get((KEYDOWN, MOUSEMOTION, MOUSEBUTTONDOWN))
        pygame.event.clear()
        if len(event):
            event = event.pop()
            if event.type == KEYDOWN:
                if event.dict['key'] == K_ESCAPE:
                    sys.exit(0)
            elif event.type == MOUSEMOTION:
                pos = event.dict['pos']
            elif event.type == MOUSEBUTTONDOWN and event.dict['button'] == 1:
                click = True
                pos = event.dict['pos']
            
        pool.update(pos, click)
        pool.clear(screen, clear_callback)
        pool.draw(screen)
        pygame.display.flip()
        screen.blit(pool.image, (0, 0))


if __name__ == '__main__':
    pygame.init()
    main()

