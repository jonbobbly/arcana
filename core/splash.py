import curses

import core
from state import State

class SplashMenu(State):
    def __init__(self):
        State.__init__(self)
        self.menu = core.GameMenu("splash.json")

    def run(self, g):
        choice = g.show_menu(self.menu)

        if choice["action"] == "debug":
            self.next_state = "Debug"
            self.done = True
        if choice["action"] == "quit":
            self.next_state = None
            self.done = True

