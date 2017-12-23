import core
from .state import State

class Dbg_arcana_list(State):
    def __init__(self, persist):
        self.persist = persist
        g = self.persist["g"]
        State.__init__(self)
        self.title = g.DisplayBox(1, 80, 0, 0)
        self.status = g.DisplayBox(1, 80, 23, 0)
        self.arcana = g.DisplayBox(21, 80, 1, 0)

    def run(self):
        g = self.persist["g"]
        self.title.erase()
        self.title.write("Arcana List")
        self.title.hilight()
        self.title.refresh()

        self.status.erase()
        self.status.write("Q|Back  J|Next  K|Prev")
        self.status.hilight()
        self.status.refresh()

        key = self.status.wait()

        if key == ord("q"):
            self.movestate("Debug")
