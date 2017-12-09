import curses

def init(stdscr):
    stdscr.clear()
    curses.curs_set(False)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)

def show_menu(gmenu, list_pad, desc_box):
    hilite = curses.color_pair(2)
    normal = curses.A_NORMAL
    gmenu.list_titles(list_pad.pad)

    start = 0
    selected = 0
    key = 0
    while key != ord('q'):
        if selected < start:
            start -= 1
        if selected > start + list_pad.dh:
            start += 1

        list_pad.pad.chgat(selected, 0, hilite)

        desc_box.box.erase()
        desc_box.box.addstr(
                gmenu.get_desc(selected)
        )

        desc_box.refresh()
        list_pad.refresh(start)

        list_pad.pad.chgat(
                selected, 0, normal
        )
        key = list_pad.pad.getch()
        if key == ord('j'):
            selected += 1
        if key == ord('k'):
            selected -= 1
        if selected < 0:
            selected = 0
        if selected >= gmenu.num_items():
            selected = gmenu.num_items()-1
        if key == ord('\n'):
            return gmenu.get_item(selected)
    return "none"

class DisplayBox():
    def __init__(self, h, w, r, c):
        self.box = curses.newwin(h, w, r, c)

    def refresh(self):
        self.box.refresh()

class ListBox():
    def __init__(self, h, w, r, c, dh):
        self.h = h
        self.w = w
        self.r = r
        self.c = c
        self.dh = dh
        self.pad = curses.newpad(h, w)

    def refresh(self, top, left = 0, h = None, w = None):
        if h == None:
            h = self.dh
        if w == None:
            w = self.w
        self.pad.refresh( top,left, self.r,self.c, h,w )
