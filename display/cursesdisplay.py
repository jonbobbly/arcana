import curses

class CursesDisplay():
    def __init__(self, stdscr):
        stdscr.clear()
        curses.curs_set(False)

        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
        self.hilite_color = curses.color_pair(2)
        self.normal_color = curses.A_NORMAL

        self.windows = { "title": curses.newwin(1, 80, 0, 0),
                         "desc": curses.newwin(10, 30, 1, 31),
                         "listpad": curses.newpad(100, 30),
                         "listwiny": 1,
                         "listwinx": 0,
                         "listwinh": 10,
                         "listwinw": 30
                       }

    def show_menu(self, gmenu):
        gmenu.list_titles(self.windows["listpad"])

        self.windows["title"].erase()
        self.windows["title"].chgat(0,0, self.hilite_color)
        self.windows["title"].addstr(
                gmenu.menu_title(), self.hilite_color
        )

        start = 0
        selected = 0
        key = 0
        while key != ord('q'):
            if selected < start:
                start -= 1
            if selected > start + self.windows["listwinh"]:
                start += 1

            self.windows["listpad"].chgat(selected, 0, self.hilite_color)

            self.windows["desc"].erase()
            self.windows["desc"].addstr(
                    gmenu.get_desc(selected)
            )

            self.windows["title"].refresh()
            self.windows["desc"].refresh()
            self.windows["listpad"].refresh(
                start, 0, 
                self.windows["listwiny"], self.windows["listwinx"],
                self.windows["listwinh"], self.windows["listwinw"]
            )

            self.windows["listpad"].chgat(
                    selected, 0, self.normal_color
            )
            key = self.windows["listpad"].getch()
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
