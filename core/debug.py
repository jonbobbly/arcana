import curses

import core
from state import State

class DebugMenu(State):
    def __init__(self):
        State.__init__(self)
        self.menu = core.GameMenu("debug.json")
        self.title_bar = curses.newwin(1, 80, 0, 0)
        self.desc_pad = curses.newwin(10, 30, 1, 31)
        self.list_pad = curses.newpad(100, 30)

    def draw(self, g):
        return g.show_menu(self.menu, self.title_bar, self.list_pad, self.desc_pad)

    def update(self, choice):
        if choice["action"] == "quit":
            self.next_state = "Splash"
            self.done = True
