# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:22:45 2023

@author: eliel
"""

'''
faca um programa em python que abra e reproduza um arquivo mp3
'''

import pygame
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()