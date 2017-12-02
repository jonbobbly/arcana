import curses

class CursesDisplay():
    def __init__(self, stdscr):
        stdscr.clear()
        curses.curs_set(False)

        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

        self.hilite_color = curses.color_pair(2)
        self.normal_color = curses.A_NORMAL

        self.title_bar = curses.newwin(1, 80, 0, 0)
        self.desc_pad = curses.newwin(10, 30, 1, 31)
        self.list_pad = curses.newpad(100, 30)
        self.list_height = 10

        self.title_bar.chgat(0,0, self.hilite_color)

    def clear(self):
        self.title_bar.erase()
        self.desc_pad.erase()
        self.list_pad.erase()

    def redraw(self, l_start = 0):
        self.title_bar.refresh()
        self.desc_pad.refresh()
        self.list_pad.refresh(l_start,0, 1,0, 10,30)

    def show_menu(self, gmenu):
        gmenu.list_titles(self.list_pad)
        self.title_bar.erase()
        self.title_bar.chgat(0,0, self.hilite_color)
        self.title_bar.addstr(gmenu.menu_title(), self.hilite_color)
        start = 0
        selected = 0
        key = 0

        while key != ord('q'):
            if selected < start:
                start -= 1
            if selected > start + self.list_height:
                start += 1

            self.list_pad.chgat(selected, 0, self.hilite_color)

            self.desc_pad.erase()
            self.desc_pad.addstr( gmenu.get_desc(selected) )

            self.redraw(start)

            self.list_pad.chgat(selected, 0, self.normal_color)
            key = self.list_pad.getch()
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
