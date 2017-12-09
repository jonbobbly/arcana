import curses

SCREEN = None

def init(stdscr):
    global SCREEN
    SCREEN = stdscr
    SCREEN.clear()
    curses.curs_set(False)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)

def clearscreen():
    global SCREEN
    SCREEN.clear()
    SCREEN.refresh()

def show_menu(gmenu, list_pad, desc_box):
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

        list_pad.hilight(selected)

        desc_box.erase()
        desc_box.write( gmenu.get_desc(selected) )
        desc_box.refresh()

        list_pad.refresh(start)     

        key = list_pad.wait()
        list_pad.hilight(selected, normal)

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

    def hilight(self, row = 0, colorpair = 2):
        self.box.chgat(row, 0, curses.color_pair(colorpair))

    def write(self, text, row = 0, col = 0):
        #This will eventually include word wrapping
        self.box.addstr(row, col, text)

    def erase(self):
        self.box.erase()

    def refresh(self):
        self.box.refresh()

    def wait(self):
        return self.box.getch()

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

    def write(self, text, row = 0, col = 0):
        #This will eventually include word wrapping
        self.pad.addstr(row, col, text)

    def hilight(self, row = 0, colorpair = 2):
        self.pad.chgat(row, 0, curses.color_pair(colorpair))

    def wait(self):
        return self.pad.getch()

    def erase(self):
        self.pad.erase()
