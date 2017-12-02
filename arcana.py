#!/usr/bin/python

import os
import curses
from curses import wrapper

import core
import display

rm = core.ResourceManager()

def main(stdscr):
    g = display.CursesDisplay(stdscr)
    states = {
            "Splash": core.SplashMenu(),
            "Debug": core.DebugMenu()
            }

    game = core.Game(g, states, "Splash")
    game.run()

wrapper(main)
