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
            "Debug": core.DebugMenu(display),
            "dbg_arcana_list": core.Dbg_arcana_list(display)
            }

    game = core.Game(display, states, "Splash")
    game.run()

wrapper(main)
