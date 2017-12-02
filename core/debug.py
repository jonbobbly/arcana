import core
from state import State

class DebugMenu(State):
    def __init__(self):
        State.__init__(self)
        self.menu = core.GameMenu("debug.json")

    def update(self, choice):
        if choice["action"] == "quit":
            self.next_state = "Splash"
            self.done = True