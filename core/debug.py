import curses

import core
from state import State

class DebugMenu(State):
    def __init__(self, g):
        State.__init__(self)
        self.menu = core.GameMenu("debug.json")
        self.title = g.DisplayBox(1, 80, 0, 0)
        self.list_pad = g.ListBox(100, 30, 1, 0, 10)
        self.desc_box = g.DisplayBox(10, 30, 1, 32)

    def run(self, g):
        self.title.box.erase()
        self.title.box.addstr(0, 0, "!!! DEBUG !!!")
        self.title.box.chgat(0, 0, curses.color_pair(3))
        self.title.refresh()

        choice = g.show_menu(self.menu, self.list_pad, self.desc_box)

        if choice["action"] == "quit":
            self.next_state = "Splash"
            self.done = True
