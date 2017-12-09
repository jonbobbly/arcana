import curses

import core
from state import State

class SplashMenu(State):
    def __init__(self, g):
        State.__init__(self)
        self.menu = core.GameMenu("splash.json")
        self.title = g.DisplayBox(1, 80, 0, 0)
        self.list_pad = g.ListBox(100, 30, 1, 0, 10)
        self.desc_box = g.DisplayBox(10, 30, 1, 32)

    def run(self, g):
        self.title.box.erase()
        self.title.box.addstr(0, 0, "Welcome!")
        self.title.box.chgat(0, 0, curses.color_pair(2))
        self.title.refresh()

        choice = g.show_menu(self.menu, self.list_pad, self.desc_box)

        if choice["action"] == "debug":
            self.next_state = "Debug"
            self.done = True
        if choice["action"] == "quit":
            self.next_state = None
            self.done = True

