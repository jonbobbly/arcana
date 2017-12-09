class State(object):
    def __init__(self):
        self.menu = None
        self.next_state = None
        self.done = False

    def enter(self):
        self.next_state = None
        self.done = False

    def exit(self):
        pass

    def run(self, g):
        pass

    def movestate(self, statename):
        self.next_state = statename
        self.done = True
