#!/usr/bin/python

import os
import curses
from curses import wrapper

import core
import display

rm = core.ResourceManager()

def main(stdscr):
    display.init(stdscr)
    states = {
            "Splash": core.SplashMenu(display),
            "Debug": core.DebugMenu(display)
            }

    game = core.Game(display, states, "Splash")
    game.run()

wrapper(main)
