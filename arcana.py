#!/usr/bin/python

import os
import curses
from curses import wrapper

import core
import display

def main(stdscr):
    persist = {"g": display,
               "res": core.ResourceManager()
              }
    persist["g"].init(stdscr)

    states = {
            "Splash": core.SplashMenu(persist),
            "Debug": core.DebugMenu(persist),
            "dbg_arcana_list": core.Dbg_arcana_list(persist)
            }

    game = core.Game(states, "Splash", persist)
    game.run()

wrapper(main)
